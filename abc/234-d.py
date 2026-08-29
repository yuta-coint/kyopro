n,k = map(int,input().split())
p = list(map(int,input().split()))
import heapq
a = p[:k-1]
heapq.heapify(a)
ans = 0
for i in range(k-1,n):
    heapq.heappush(a, p[i])
    ans = max(ans,heapq.heappop(a))
    print(ans)