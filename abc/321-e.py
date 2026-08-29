import sys
sys.setrecursionlimit(10**7)
T=int(input())
def f(n,y,l):
    #二進数でyにl桁を足したもの
    if n+1>(y+1)*(1<<l):
        return 1<<l
    elif n+1>y*(1<<l):
        return n+1-y*(1<<l)
    else:
        return 0
for case in range(T):
    N,X,K = map(int,input().split())
    if K>300:
        print(0)
        continue
    ans = f(N,X,K)
    for i in range(1,130):
        if X==1 or K-i<0:
            break
        if K-i==0:
            ans+=1
        else:
            ans+=f(N,X^1,K-1-i)
        X>>=1
    print(ans)