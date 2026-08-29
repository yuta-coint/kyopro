N=  int(input())
A = list(map(int,input().split()))
#「下の餅」と「上の餅」を選べば、順番に並べるのが最適戦略
ok = 0
ng = N//2+1
while ok+1<ng:
    K = (ok+ng)//2
    for i in range(K):
        if A[i]>A[N-K+i]//2:
            ng = K
            break
    else:
        ok = K
print(ok)