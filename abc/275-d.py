N = int(input())
from heapq import heapify,heappop,heappush
q = [-N]
heapify(q)
big = 10**6
cal = [0 for i in range(big+1)]
d = {N:1}
cnt = 1
while cnt>0:
    t = -heappop(q)
    #print(t)
    cnt-=1
    if t<=big:
        cal[t]+=d[t]
    else:
        if t//2 in d:
            d[t//2]+=d[t]
        else:
            d[t//2]=d[t]
            heappush(q,-(t//2)) 
            cnt+=1
        if t//3 in d:
            d[t//3]+=d[t]
        else:
            d[t//3]=d[t]
            heappush(q,-(t//3))  
            cnt+=1  
dp = [0 for i in range(big+1)]
dp[0]=1
for i in range(1,big+1):
    dp[i]=dp[i//2]+dp[i//3]
ans = 0
for i in range(big+1):
    ans+=dp[i]*cal[i]
print(ans)
