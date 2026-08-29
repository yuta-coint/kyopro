t = int(input())
import sys
input = sys.stdin.readline
for i in range(t):
    n,m = map(int,input().split())
    ans = 0
    if n>m:
        n,m = m,n
    if n==1 and m>2:
        ans = -1
    elif m==n:
        ans = 2*(n-1)
    else:
        ans = 2*n-1
        m-=n+1
        if m&1:
            ans+=(m>>1)*4+3
        else:
            ans+=(m>>1)*4
    print(ans)

