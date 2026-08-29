import sys
from math import gcd
from bisect import bisect
from functools import cmp_to_key


def _line_cmp(l1, l2):
    # 傾き pn/d の昇順、等しければ切片 qn/d の昇順で比較する。
    # d > 0 に正規化してあるので、たすき掛けでそのまま比較できる。
    a = l1[0] * l2[2]   # pn1 * d2
    b = l2[0] * l1[2]   # pn2 * d1
    if a != b:
        return -1 if a < b else 1
    a = l1[1] * l2[2]   # qn1 * d2
    b = l2[1] * l1[2]   # qn2 * d1
    if a != b:
        return -1 if a < b else 1
    return 0


class UpperEnvelope:
    def __init__(self):
        # 各直線を (pn, qn, d, data) として保持する。
        #   傾き   slope     = pn / d
        #   切片   intercept = qn / d
        # d > 0 になるよう正規化する。
        self.lines = []

    def add_line(self, A, B, C, data=None):
        """
        AX + BY = C の直線を追加する。
        内部では Y = (-A/B)X + (C/B) とみなす。
        """
        if B == 0:
            # 垂直な線は Y = f(X) の包絡線に寄与しないため無視する
            return

        # B が正になるように符号を調整
        if B < 0:
            A, B, C = -A, -B, -C

        pn, qn, d = -A, C, B  # slope = pn/d, intercept = qn/d, d > 0

        # 整数を小さく保つため gcd で約分（slope と intercept は同じ分母 d を共有）
        g = gcd(gcd(pn, qn), d)
        if g > 1:
            pn //= g
            qn //= g
            d //= g

        self.lines.append((pn, qn, d, data))

    def build(self, filter_x_ge_0=False):
        """
        上側包絡線を構築し、構成する直線のリストを傾きの昇順で返す。
        各要素は (pn, qn, d, data)。
        filter_x_ge_0 = True の場合、X >= 0 の領域で常に劣後する直線を排除する。
        """
        if not self.lines:
            return []

        # 1. 傾き昇順、等しければ切片昇順にソート（整数比較）
        self.lines.sort(key=cmp_to_key(_line_cmp))

        # 2. 傾きが完全に同じ直線は、切片が最大のもの（一番上）だけを残す。
        #    ソート済みなので、傾きが等しいなら後ろの要素ほど切片が大きい。
        unique_lines = []
        for line in self.lines:
            if unique_lines:
                last = unique_lines[-1]
                # 傾きが等しいか（pn1/d1 == pn2/d2 <=> pn1*d2 == pn2*d1）
                if last[0] * line[2] == line[0] * last[2]:
                    unique_lines[-1] = line
                    continue
            unique_lines.append(line)

        # 3. [オプション] X >= 0 で完全に劣後する直線を排除
        if filter_x_ge_0:
            filtered = []
            max_qn = None
            max_d = None
            # 傾きが大きい方（右側）から走査し、切片の最大値を更新できないものを弾く
            for line in reversed(unique_lines):
                qn, d = line[1], line[2]
                # qn/d > max_qn/max_d <=> qn*max_d > max_qn*d （d, max_d > 0）
                if max_qn is None or qn * max_d > max_qn * d:
                    filtered.append(line)
                    max_qn, max_d = qn, d
            filtered.reverse()
            unique_lines = filtered

        # 4. 上側包絡線の構築（Graham-scan ライク）
        #    交点 X の大小をたすき掛けで比較する。
        #    L1,L2 の交点 x12 = (qn1*d2 - qn2*d1) / (pn2*d1 - pn1*d2)
        #    L2,L3 の交点 x23 = (qn2*d3 - qn3*d2) / (pn3*d2 - pn2*d3)
        #    （分母の d1*d2 等は約分されて消える。傾きは狭義昇順なので分母は必ず正。）
        envelope = []
        for line in unique_lines:
            pn3, qn3, d3 = line[0], line[1], line[2]
            while len(envelope) >= 2:
                pn1, qn1, d1 = envelope[-2][0], envelope[-2][1], envelope[-2][2]
                pn2, qn2, d2 = envelope[-1][0], envelope[-1][1], envelope[-1][2]

                x12_num = qn1 * d2 - qn2 * d1
                x12_den = pn2 * d1 - pn1 * d2   # > 0
                x23_num = qn2 * d3 - qn3 * d2
                x23_den = pn3 * d2 - pn2 * d3   # > 0

                # x12 >= x23  <=>  x12_num*x23_den >= x23_num*x12_den （両分母 > 0）
                if x12_num * x23_den >= x23_num * x12_den:
                    envelope.pop()
                else:
                    break
            envelope.append(line)

        return envelope


# --- 以下、問題の解答部分 ---

def inclination_compare(p, q):
    # p/q が小さい順にソート
    if p[0] * q[1] < p[1] * q[0]:
        return -1
    elif p[0] * q[1] > p[1] * q[0]:
        return 1
    else:
        return 0


def solve():
    input_data = sys.stdin.read().split()
    if not input_data:
        return

    N = int(input_data[0])
    idx = 1

    env = UpperEnvelope()

    for _ in range(N):
        A = int(input_data[idx])
        B = int(input_data[idx + 1])
        # 双対平面上の直線 Y = -A X + B として扱う（Ax + y = B に対応）
        env.add_line(A, 1, B, data=(A, B))
        idx += 2

    # X >= 0 の領域に限定して包絡線を構築
    envelope_lines = env.build(filter_x_ge_0=True)

    # envelope_lines は傾き（-A）昇順 = A 降順。
    # 二分探索用に A 昇順にするため反転する。
    new_AB = [line[3] for line in envelope_lines]
    new_AB.reverse()

    Q = int(input_data[idx])
    idx += 1

    wrapper = cmp_to_key(inclination_compare)
    out = []

    for _ in range(Q):
        C = int(input_data[idx])
        D = int(input_data[idx + 1])
        idx += 2

        s = bisect(new_AB, wrapper((C, D)), key=wrapper)

        if s == 0:
            out.append("-1")
        elif s == len(new_AB):
            out.append(str(D / new_AB[-1][1]))
        else:
            p0 = new_AB[s - 1]
            p1 = new_AB[s]
            ans = (-C * (p1[1] - p0[1]) + D * (p1[0] - p0[0])) / (p0[1] * p1[0] - p0[0] * p1[1])
            out.append(str(ans))

    print('\n'.join(out))


if __name__ == '__main__':
    solve()