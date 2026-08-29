N = int(input())
P = list(map(int,input().split()))
from heapq import heapify,heappop,heappush
ans = 0
hand = [(P[0],0)]
heapify(hand)
ans = 0
for i in range(1,N):
    t,s = heappop(hand)
    if t<P[i]:
        ans+=P[i]-t
        if s==1:
            heappush(hand,(t,0))
        heappush(hand,(P[i],1))
    else:
        heappush(hand,(t,s))
        heappush(hand,(P[i],0))
print(ans)