def main():
    N = int(input())
    p = list(map(lambda x:int(x)-1,input().split()))
    q = list(map(lambda x:int(x)-1,input().split()))
    mod = 998244353
    pq = [(p[i],q[i]) for i in range(N)]
    pq.sort()
    q = [pq[i][1] for i in range(N)]
    dpb = [0 for i in range(N)]
    dpw = [0 for i in range(N)]
    dpb[0]=1
    dpw[0]=1
    for i in range(1,N):
        dpw[i] = dpw[i-1]+dpb[i-1]
        dpw[i]%=mod
        dpb[i] = dpw[i-1]
    #print(dpb)
    #print(dpw)
    chk  = [False for i in range(N)]
    ans = 1
    for i in range(N):
        if chk[i]:
            continue
        t = i
        cnt=1
        while True:
            chk[t]=True
            if q[t]==i:
                break
            t = q[t]
            cnt+=1
        #print(cnt)
        if cnt==1:
            continue
        elif cnt==2:
            ans*=3
        elif cnt==3:
            ans*=4
        else:
            ans*=(dpw[cnt-4]+dpb[cnt-4]+dpw[cnt-2]+dpb[cnt-2])%mod
        ans%=mod
    print(ans)
main()