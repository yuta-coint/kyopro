N,M = map(int,input().split())
L = list(map(int,input().split()))
ok = 10**16
ng = max(L)-1
while ng+1<ok:
    W = (ok+ng)//2
    line = 0
    let = 0
    for i in range(N):
        if let==0:
            let+=L[i]
        elif let+1+L[i]<=W:
            let = let+1+L[i]
        else:
            line+=1
            let = L[i]
    if line<M:
        ok = W
    else:
        ng = W
print(ok)