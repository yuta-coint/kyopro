import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
a = [[0 for _ in range(i+1)]+list(map(int,input().split())) for i in range(2*n)]
#print(a)
#残りのビット、金額、bit数
ans = 0
def enjoy(k,b,e):
    global ans
    if b == 2*n:
        ans = max(ans,e)
    else:
        for i in range(2*n):
            if k>>i&1:
                target = i
                break
        for i in range(target+1,2*n):
            if k>>i&1:
                enjoy(k-2**i-2**target,b+2,a[target][i]^e)
enjoy(2**(2*n)-1,0,0)
print(ans)