import typing
class FenwickTree:
    '''Reference: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_B'''
    #1から数える
    def __init__(self, n: int = 0) -> None:
        self._n = n
        self.data = [0] * n
    #p番目にxを足す
    def add(self, p: int, x: typing.Any) -> None:
        assert 0 <= p < self._n

        p += 1
        while p <= self._n:
            self.data[p - 1] += x
            p += p & -p
    #[left,right)
    def sum(self, left: int, right: int) -> typing.Any:
        assert 0 <= left <= right <= self._n

        return self._sum(right) - self._sum(left)

    def _sum(self, r: int) -> typing.Any:
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r

        return s
N,Q = map(int,input().split())
BIT = FenwickTree(N+1)
for i in range(Q):
    com,x,y = map(int,input().split())
    if com==0:
        BIT.add(x,y)
    else:
        print(BIT.sum(x,y+1))
