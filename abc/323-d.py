from heapq import heapify,heappop,heappush
N = int(input())
q = []
heapify(q)
for i in range(N):
    S,C = map(int,input().split())
    heappush(q,(S,C))
ans = 0
cnt = N
while cnt>0:
    S1,C1 = heappop(q)
    cnt-=1
    if cnt>0:
        S2,C2 = heappop(q)
        cnt-=1
        if S1==S2:
            heappush(q,(S1,C1+C2))
            cnt+=1
            continue
        heappush(q,(S2,C2))
        cnt+=1
    if C1&1:
        ans += 1
    if C1//2>0:
        heappush(q,(2*S1,C1//2))
        cnt+=1
print(ans)