N,L=map(int,input().split())
A= list(map(int,input().split()))
if sum(A)<L:
    A.append(L-sum(A))
    N+=1
from heapq import heappush, heappop
hq = []
for i in range(N):
    heappush(hq,A[i])
ans=0
for i in range(N-1):
    t = heappop(hq)
    s = heappop(hq)
    ans+=s+t
    heappush(hq,s+t)
print(ans)


