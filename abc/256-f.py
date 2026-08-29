import sys
input = sys.stdin.readline
N,Q = map(int,input().split())
mod = 998244353
a = list(map(int,input().split()))
import typing
def main():
    class FenwickTree:
        '''Reference: https://onlinejudge.u-aizu.ac.jp/courses/library/3/DSL/2/DSL_2_B'''

        def __init__(self, n: int = 0) -> None:
            self._n = n
            self.data = [0] * n
        #p番目にxを足す
        def add(self, p: int, x: typing.Any) -> None:
            x%=mod
            assert 0 <= p < self._n
            p += 1
            while p <= self._n:
                self.data[p - 1] += x
                self.data[p - 1] %= mod
                p += p & -p
        def sum(self, left: int, right: int) -> typing.Any:
            assert 0 <= left <= right <= self._n

            return self._sum(right) - self._sum(left)

        def _sum(self, r: int) -> typing.Any:
            s = 0
            while r > 0:
                s += self.data[r - 1]
                s %= mod
                r -= r & -r

            return s
    #Ax…そのまま
    #Bx…左からiこ足し上げる
    #Cx…i個目のものにはAjがi-j個足されている
    #Dx…iコメのものにはAjが(i-j)(i-j+1)/2個足されている
    #i個目のものにAjがi*i個足されている
    #
    Seg0 = FenwickTree(N+1)
    Seg1 = FenwickTree(N+1)
    Seg2 = FenwickTree(N+1)
    for i in range(1,N+1):
        Seg0.add(i,a[i-1])
        Seg1.add(i,a[i-1]*i)
        Seg2.add(i,a[i-1]*i*i)
    for i in range(Q):
        query = list(map(int,input().split()))
        if query[0]==1:
            x,v = query[1],query[2]
            s = Seg0.sum(x,x+1)
            Seg0.add(x,v-s)
            s = Seg1.sum(x,x+1)
            Seg1.add(x,v*x-s)
            s = Seg2.sum(x,x+1)
            Seg2.add(x,v*x*x-s)
        elif query[0]==2:
            x = query[1]
            print(((Seg2._sum(x+1)-Seg1._sum(x+1)*(2*x+3)+Seg0._sum(x+1)*(x+1)*(x+2))*499122177)%mod)
main()