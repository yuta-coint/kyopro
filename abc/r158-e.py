##迂回することを考えていない嘘回答です。
# https://github.com/tatyam-prime/SortedSet/blob/main/SortedSet.py
import math
from bisect import bisect_left, bisect_right
from typing import Generic, Iterable, Iterator, TypeVar, Optional, List
T = TypeVar('T')
class SortedSet(Generic[T]):
    BUCKET_RATIO = 50
    REBUILD_RATIO = 170

    def _build(self, a=None) -> None:
        "Evenly divide `a` into buckets."
        if a is None: a = list(self)
        size = self.size = len(a)
        bucket_size = int(math.ceil(math.sqrt(size / self.BUCKET_RATIO)))
        self.a = [a[size * i // bucket_size : size * (i + 1) // bucket_size] for i in range(bucket_size)]
    
    def __init__(self, a: Iterable[T] = []) -> None:
        "Make a new SortedSet from iterable. / O(N) if sorted and unique / O(N log N)"
        a = list(a)
        if not all(a[i] < a[i + 1] for i in range(len(a) - 1)):
            a = sorted(set(a))
        self._build(a)

    def __iter__(self) -> Iterator[T]:
        for i in self.a:
            for j in i: yield j

    def __reversed__(self) -> Iterator[T]:
        for i in reversed(self.a):
            for j in reversed(i): yield j
    
    def __len__(self) -> int:
        return self.size
    
    def __repr__(self) -> str:
        return "SortedSet" + str(self.a)
    
    def __str__(self) -> str:
        s = str(list(self))
        return "{" + s[1 : len(s) - 1] + "}"

    def _find_bucket(self, x: T) -> List[T]:
        "Find the bucket which should contain x. self must not be empty."
        for a in self.a:
            if x <= a[-1]: return a
        return a

    def __contains__(self, x: T) -> bool:
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        return i != len(a) and a[i] == x

    def add(self, x: T) -> bool:
        "Add an element and return True if added. / O(√N)"
        if self.size == 0:
            self.a = [[x]]
            self.size = 1
            return True
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i != len(a) and a[i] == x: return False
        a.insert(i, x)
        self.size += 1
        if len(a) > len(self.a) * self.REBUILD_RATIO:
            self._build()
        return True

    def discard(self, x: T) -> bool:
        "Remove an element and return True if removed. / O(√N)"
        if self.size == 0: return False
        a = self._find_bucket(x)
        i = bisect_left(a, x)
        if i == len(a) or a[i] != x: return False
        a.pop(i)
        self.size -= 1
        if len(a) == 0: self._build()
        return True
    
    def lt(self, x: T) -> Optional[T]:
        "Find the largest element < x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] < x:
                return a[bisect_left(a, x) - 1]

    def le(self, x: T) -> Optional[T]:
        "Find the largest element <= x, or None if it doesn't exist."
        for a in reversed(self.a):
            if a[0] <= x:
                return a[bisect_right(a, x) - 1]

    def gt(self, x: T) -> Optional[T]:
        "Find the smallest element > x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] > x:
                return a[bisect_right(a, x)]

    def ge(self, x: T) -> Optional[T]:
        "Find the smallest element >= x, or None if it doesn't exist."
        for a in self.a:
            if a[-1] >= x:
                return a[bisect_left(a, x)]
    
    def __getitem__(self, x: int) -> T:
        "Return the x-th element, or IndexError if it doesn't exist."
        if x < 0: x += self.size
        if x < 0: raise IndexError
        for a in self.a:
            if x < len(a): return a[x]
            x -= len(a)
        raise IndexError
    
    def index(self, x: T) -> int:
        "Count the number of elements < x."
        ans = 0
        for a in self.a:
            if a[-1] >= x:
                return ans + bisect_left(a, x)
            ans += len(a)
        return ans

    def index_right(self, x: T) -> int:
        "Count the number of elements <= x."
        ans = 0
        for a in self.a:
            if a[-1] > x:
                return ans + bisect_right(a, x)
            ans += len(a)
        return ans
mod = 998244353
ans = 0
N = int(input())
x1 = list(map(int,input().split()))
x2 = list(map(int,input().split()))
left_x1 = [x1[0]]
right_x2 = [sum(x2)]
left_x2 = [x2[0]]
right_x1 = [sum(x1)]
for i in range(N-1):
    left_x1.append(left_x1[-1]+x1[i+1])
    right_x2.append(right_x2[-1]-x2[i])
    left_x2.append(left_x2[-1]+x2[i+1])
    right_x1.append(right_x1[-1]-x1[i])
black = [(left_x1[i]+right_x2[i],i) for i in range(N)]
white = [(left_x2[i]+right_x1[i],i) for i in range(N)]
black.sort()
white.sort()
#blackの処理
b_ss = SortedSet(a=[-1,N])
for i in range(N):
    x,k = black[i]
    x%=mod
    #print((k-b_ss.le(k))*(b_ss.ge(k)-k),k)
    ans += (k-b_ss.le(k))*(b_ss.ge(k)-k)%mod*x%mod
    ans %= mod
    b_ss.add(k)
#print(ans)
w_ss = SortedSet(a=[-1,N])
for i in range(N):
    x,k = white[i]
    ans += (k-w_ss.le(k))*(w_ss.ge(k)-k)%mod*x%mod
    #print((k-w_ss.le(k))*(w_ss.ge(k)-k),k)
    ans %= mod
    w_ss.add(k)
#print(ans)
#累積和から引くべきやつら
for i in range(N):
    ans -= (left_x1[i]+left_x2[i])%mod*(N-1-i)%mod
    ans%=mod
    ans -= (right_x1[i]+right_x2[i])%mod*i%mod
    ans%=mod
#print(ans)
#とりあえず上上と下下を数える。
for i in range(N):
    ans += (x1[i]+x2[i])%mod*(i+1)%mod*(N-i)%mod
    ans%=mod
#print(ans)
ans *= 2
ans -= (sum(x1)+sum(x2))%mod*3%mod
ans %= mod
print(ans)