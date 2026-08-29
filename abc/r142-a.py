N,K=map(int,input().split())
if K%10==0:
    ans = 0
else:
    lK = len(str(K))
    k2 = 0
    sK=str(K)
    for i in range(lK):
        k2+=int(sK[i])*(10**i)
    #print(k2)
    if K>k2:
        ans=0
    else:
        ans=0
        if K!=k2:
            while K<=N:
                ans+=1
                K*=10
        while k2<=N:
            ans+=1
            k2*=10
print(ans)