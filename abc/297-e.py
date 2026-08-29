N,K = map(int,input().split())
A = list(map(int,input().split()))
added = set()
cnt = 0
from heapq import heapify,heappop,heappush
q = [0]
heapify(q)
while True:
    x=heappop(q)
    if cnt==K:
        print(x)
        break
    cnt+=1
    for i in range(N):
        if x+A[i] in added:
            continue
        else:
            heappush(q,x+A[i])
            added.add(x+A[i])