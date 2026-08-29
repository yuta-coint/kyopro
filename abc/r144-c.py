N,K=map(int,input().split())
if N//2<K:
    print(-1)
else:
    ans = []
    t = N//(K*2)
    cnt=0
    for i in range(t-1):
        for j in range(K):
            cnt+=1
            ans.append(cnt+K)
        for j in range(K):
            cnt+=1
            ans.append(cnt-K)
    rem = K*2+N%(K*2)
    cnt2 = cnt
    if rem<=3*K:
        for i in range(rem-K):
            cnt+=1
            ans.append(cnt+K)
        for i in range(1,K+1):
            ans.append(cnt2+i)
    else:
        for i in range(K):
            cnt+=1
            ans.append(cnt+K)
        for i in range(1,rem%K+1):
            cnt2+=1
            cnt+=1
            ans.append(cnt2)
        for i in range(K):
            cnt+=1
            ans.append(cnt+K)
        for i in range(K-rem%K):
            cnt+=1
            cnt2+=1
            ans.append(cnt2)
        for i in range(rem%K):
            cnt+=1
            ans.append(cnt-K)    
    print(*ans)
    
