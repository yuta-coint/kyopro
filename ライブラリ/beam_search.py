#https://eijirou-kyopro.hatenablog.com/entry/2024/02/01/115639
"""二重連鎖木を用いるビームサーチのテンプレート（Python 3.10 以降）。

元の C++ コードの探索順・候補選択・同点時の扱いを維持している。
Action / Evaluator / State の TODO を問題に合わせて実装すること。

注意:
* Python には list.reserve() がないため、reserve と nodes_capacity は
  互換性のために残しているが、メモリの事前確保は行わない。
* Action / Evaluator は Python オブジェクトとして参照で保持する。
  selector.push() や Node() に渡した後は変更せず、新しいオブジェクトを
  作って次の候補を表すこと（リストなどの内部データの共有にも注意）。
* Tree は最初に State を deepcopy する。共有したい入力データがある場合は、
  State.__deepcopy__ を実装するなどして調整できる。
* C++ の uint32_t と違い、Python の int は自動で 32 bit に丸められない。
  必要ならハッシュ計算側で & 0xFFFFFFFF を適用すること。
"""

from __future__ import annotations

import sys
from copy import deepcopy
from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar("T")


class ObjectPool(Generic[T]):
    """解放されたインデックスを再利用するプール。"""

    __slots__ = ("data_", "garbage_")

    def __init__(self) -> None:
        self.data_: list[T] = []
        self.garbage_: list[int] = []

    def __getitem__(self, i: int) -> T:
        return self.data_[i]

    def reserve(self, capacity: int) -> None:
        # Python の list には reserve がない。
        pass

    def push(self, x: T) -> int:
        """要素を追加し、追加されたインデックスを返す。"""
        if not self.garbage_:
            self.data_.append(x)
            return len(self.data_) - 1
        i = self.garbage_.pop()
        self.data_[i] = x
        return i

    def pop(self, i: int) -> None:
        """要素を見かけ上削除する。同じ i を二重に解放しないこと。"""
        self.garbage_.append(i)

    def size(self) -> int:
        """使用した最大のインデックス + 1（現在の有効要素数ではない）。"""
        return len(self.data_)


class HashMap(Generic[T]):
    """整数キーにハッシュ関数を適用しない線形探索法の連想配列。

    n は 1 回の clear() までに登録するキーの数より十分大きくする。
    元コードと同様、満杯になると get_index() の探索が終了しない。
    Selector は候補を置き換えても古いキーを削除しない点に注意。
    """

    __slots__ = ("n_", "valid_", "keys_", "values_")

    def __init__(self, n: int) -> None:
        if n <= 0:
            raise ValueError("hash_map_capacity must be positive")
        self.n_ = n
        self.valid_ = bytearray(n)
        self.keys_: list[int] = [0] * n
        self.values_: list[T | None] = [None] * n

    def get_index(self, key: int) -> tuple[bool, int]:
        """(存在するか, 格納位置または空き位置) を返す。"""
        i = key % self.n_
        while self.valid_[i]:
            if self.keys_[i] == key:
                return True, i
            i += 1
            if i == self.n_:
                i = 0
        return False, i

    def set(self, i: int, key: int, value: T) -> None:
        self.valid_[i] = 1
        self.keys_[i] = key
        self.values_[i] = value

    def get(self, i: int) -> T:
        assert self.valid_[i]
        return self.values_[i]  # type: ignore[return-value]

    def clear(self) -> None:
        self.valid_ = bytearray(self.n_)


Hash = int  # TODO
Cost = int  # TODO: 変更する場合は MaxSegtree の単位元も確認すること。


@dataclass(slots=True)
class Action:
    """状態遷移に必要な情報。なるべく小さくすること。"""

    # TODO: フィールドや初期値を定義する。
    pass


@dataclass(slots=True)
class Evaluator:
    """状態のコストを評価するための情報。なるべく小さくすること。"""

    # TODO: フィールドや初期値を定義する。

    def evaluate(self) -> Cost:
        """小さいほどよいコストを返す。"""
        # TODO
        raise NotImplementedError


@dataclass(slots=True)
class Candidate:
    action: Action
    evaluator: Evaluator
    hash: Hash
    parent: int
    cost: Cost


@dataclass(slots=True)
class Config:
    max_turn: int
    beam_width: int
    nodes_capacity: int
    hash_map_capacity: int


class MaxSegtree:
    """(コスト, 候補番号) を管理する最大値セグメント木。

    コストが同じなら左側を選ぶ。tuple の max() とは同点時の挙動が異なる。
    """

    __slots__ = ("size_", "data_")

    def __init__(self, values: list[tuple[Cost, int]]) -> None:
        size = 1
        while size < len(values):
            size <<= 1
        self.size_ = size
        self.data_: list[tuple[int | float, int]] = [
            (float("-inf"), -1)
        ] * (2 * size)
        self.data_[size : size + len(values)] = values
        for i in range(size - 1, 0, -1):
            a = self.data_[i << 1]
            b = self.data_[(i << 1) | 1]
            self.data_[i] = a if a[0] >= b[0] else b

    def set(self, i: int, value: tuple[Cost, int]) -> None:
        i += self.size_
        self.data_[i] = value
        i >>= 1
        while i:
            a = self.data_[i << 1]
            b = self.data_[(i << 1) | 1]
            self.data_[i] = a if a[0] >= b[0] else b
            i >>= 1

    def all_prod(self) -> tuple[int | float, int]:
        return self.data_[1]


class Selector:
    """評価のよい候補をビーム幅だけ選び、同一ハッシュをまとめる。"""

    __slots__ = (
        "beam_width", "candidates_", "hash_to_index_", "full_", "st_",
        "finished_candidates_",
    )

    def __init__(self, config: Config) -> None:
        if config.beam_width <= 0:
            raise ValueError("beam_width must be positive")
        self.beam_width = config.beam_width
        self.candidates_: list[Candidate] = []
        self.hash_to_index_ = HashMap[int](config.hash_map_capacity)
        self.full_ = False
        self.st_ = MaxSegtree([])
        self.finished_candidates_: list[Candidate] = []

    def push(
        self,
        action: Action,
        evaluator: Evaluator,
        hash: Hash,
        parent: int,
        finished: bool,
    ) -> None:
        """候補を追加する。

        finished=True は、ターン数最小化型の問題でこの遷移により
        実行可能解が得られる場合にのみ指定する。
        """
        cost = evaluator.evaluate()
        if finished:
            self.finished_candidates_.append(
                Candidate(action, evaluator, hash, parent, cost)
            )
            return

        if self.full_ and cost >= self.st_.all_prod()[0]:
            return

        valid, i = self.hash_to_index_.get_index(hash)
        if valid:
            j = self.hash_to_index_.get(i)
            if hash == self.candidates_[j].hash:
                if cost < self.candidates_[j].cost:
                    self.candidates_[j] = Candidate(
                        action, evaluator, hash, parent, cost
                    )
                    if self.full_:
                        self.st_.set(j, (cost, j))
                return

        if self.full_:
            j = self.st_.all_prod()[1]
            self.hash_to_index_.set(i, hash, j)
            self.candidates_[j] = Candidate(action, evaluator, hash, parent, cost)
            self.st_.set(j, (cost, j))
        else:
            self.hash_to_index_.set(i, hash, len(self.candidates_))
            self.candidates_.append(Candidate(action, evaluator, hash, parent, cost))
            if len(self.candidates_) == self.beam_width:
                self.construct_segment_tree()

    def select(self) -> list[Candidate]:
        """選んだ候補を返す。返されたリストは変更しないこと。"""
        return self.candidates_

    def have_finished(self) -> bool:
        return bool(self.finished_candidates_)

    def get_finished_candidates(self) -> list[Candidate]:
        return self.finished_candidates_

    def clear(self) -> None:
        self.candidates_.clear()
        self.hash_to_index_.clear()
        self.full_ = False
        # 元コードと同様、finished_candidates_ は消去しない。
        # beam_search() は実行可能解を見つけたターンで return する。

    def construct_segment_tree(self) -> None:
        self.full_ = True
        self.st_ = MaxSegtree([
            (candidate.cost, i) for i, candidate in enumerate(self.candidates_)
        ])


class State:
    """深さ優先探索に沿って更新する状態。"""

    def __init__(self) -> None:
        # TODO: 必要なら input などを引数に追加する。
        raise NotImplementedError

    def expand(
        self,
        evaluator: Evaluator,
        hash: Hash,
        parent: int,
        selector: Selector,
    ) -> None:
        """次の状態候補をすべて selector.push() に渡す。

        evaluator: 今の評価器。
        hash: 今のハッシュ値。
        parent: 今のノード ID（次のノードにとって親となる）。
        このメソッドから戻るときは現在の状態を保つこと。
        """
        # TODO
        raise NotImplementedError

    def move_forward(self, action: Action) -> None:
        """action を実行して次の状態に遷移する。"""
        # TODO
        raise NotImplementedError

    def move_backward(self, action: Action) -> None:
        """親から action で到達した現在の状態を、その親の状態へ戻す。"""
        # TODO
        raise NotImplementedError


@dataclass(slots=True)
class Node:
    """探索木のノード。Node(action, evaluator, hash) で根を作る。"""

    action: Action
    evaluator: Evaluator
    hash: Hash
    parent: int = -1
    child: int = -1
    left: int = -1
    right: int = -1

    @classmethod
    def from_candidate(cls, candidate: Candidate, right: int) -> Node:
        """C++ の通常ノード用コンストラクタに相当する。"""
        return cls(
            action=candidate.action,
            evaluator=candidate.evaluator,
            hash=candidate.hash,
            parent=candidate.parent,
            right=right,
        )


class Tree:
    """二重連鎖木と、現在位置に対応する State を管理する。"""

    __slots__ = ("state_", "nodes_", "root_")

    def __init__(self, state: State, nodes_capacity: int, root: Node) -> None:
        self.state_ = deepcopy(state)
        self.nodes_ = ObjectPool[Node]()
        self.nodes_.reserve(nodes_capacity)
        # リンクを書き換えるため、呼び出し元の root 自体は共有しない。
        self.root_ = self.nodes_.push(Node(
            action=root.action,
            evaluator=root.evaluator,
            hash=root.hash,
            parent=root.parent,
            child=root.child,
            left=root.left,
            right=root.right,
        ))

    def dfs(self, selector: Selector) -> None:
        """状態を更新しながら各葉を展開する（再帰は使わない）。"""
        self.update_root()
        v = self.root_
        while True:
            v = self.move_to_leaf(v)
            node = self.nodes_[v]
            self.state_.expand(node.evaluator, node.hash, v, selector)
            v = self.move_to_ancestor(v)
            if v == self.root_:
                break
            v = self.move_to_right(v)

    def get_path(self, v: int) -> list[Action]:
        """元の根から v までの操作列を返す。"""
        path: list[Action] = []
        while self.nodes_[v].parent != -1:
            path.append(self.nodes_[v].action)
            v = self.nodes_[v].parent
        path.reverse()
        return path

    def add_leaf(self, candidate: Candidate) -> int:
        parent = candidate.parent
        sibling = self.nodes_[parent].child
        v = self.nodes_.push(Node.from_candidate(candidate, sibling))
        self.nodes_[parent].child = v
        if sibling != -1:
            self.nodes_[sibling].left = v
        return v

    def remove_if_leaf(self, v: int) -> None:
        if self.nodes_[v].child == -1:
            self.remove_leaf(v)

    def get_best_leaf(self, last_nodes: list[int]) -> int:
        assert last_nodes
        ret = last_nodes[0]
        for v in last_nodes:
            if (
                self.nodes_[v].evaluator.evaluate()
                < self.nodes_[ret].evaluator.evaluate()
            ):
                ret = v
        return ret

    def update_root(self) -> None:
        """根から一本道になっている部分の往復を省く。"""
        child = self.nodes_[self.root_].child
        while child != -1 and self.nodes_[child].right == -1:
            self.root_ = child
            self.state_.move_forward(self.nodes_[child].action)
            child = self.nodes_[child].child

    def move_to_leaf(self, v: int) -> int:
        child = self.nodes_[v].child
        while child != -1:
            v = child
            self.state_.move_forward(self.nodes_[child].action)
            child = self.nodes_[child].child
        return v

    def move_to_ancestor(self, v: int) -> int:
        while v != self.root_ and self.nodes_[v].right == -1:
            self.state_.move_backward(self.nodes_[v].action)
            v = self.nodes_[v].parent
        return v

    def move_to_right(self, v: int) -> int:
        self.state_.move_backward(self.nodes_[v].action)
        v = self.nodes_[v].right
        self.state_.move_forward(self.nodes_[v].action)
        return v

    def remove_leaf(self, v: int) -> None:
        """不要な葉と、子がなくなった先祖を削除する（再帰は使わない）。"""
        while True:
            left = self.nodes_[v].left
            right = self.nodes_[v].right
            if left == -1:
                parent = self.nodes_[v].parent
                if parent == -1:
                    raise RuntimeError("ERROR: root is removed")
                self.nodes_.pop(v)
                self.nodes_[parent].child = right
                if right != -1:
                    self.nodes_[right].left = -1
                    return
                v = parent
            else:
                self.nodes_.pop(v)
                self.nodes_[left].right = right
                if right != -1:
                    self.nodes_[right].left = left
                return


def beam_search(config: Config, state: State, root: Node) -> list[Action]:
    """ビームサーチを行い、選ばれた操作列を返す。

    max_turn と beam_width は正の整数とする。
    ターン数最小化型では、最初に実行可能解が見つかった深さの
    finished 候補のうち最初のものを返す（元コードと同じ）。
    """
    if config.max_turn <= 0:
        raise ValueError("max_turn must be positive")

    tree = Tree(state, config.nodes_capacity, root)
    curr_nodes: list[int] = []
    next_nodes: list[int] = []
    selector = Selector(config)

    for turn in range(config.max_turn):
        tree.dfs(selector)

        if selector.have_finished():
            candidate = selector.get_finished_candidates()[0]
            ret = tree.get_path(candidate.parent)
            ret.append(candidate.action)
            return ret

        for candidate in selector.select():
            next_nodes.append(tree.add_leaf(candidate))

        if not next_nodes:
            print("ERROR: Failed to find any valid solution", file=sys.stderr)
            return []

        for v in curr_nodes:
            tree.remove_if_leaf(v)

        curr_nodes, next_nodes = next_nodes, curr_nodes
        next_nodes.clear()
        selector.clear()

    best_leaf = tree.get_best_leaf(curr_nodes)
    return tree.get_path(best_leaf)
