from heapq import heapify,heappop,heappush
N = int(input())
A = list(map(int,input().split()))
m = min(A)
A = [-A[i] for i in range(N)]
heapify(A)
cnt = 0
while N>=2:
    cnt+=1
    t = -heappop(A)
    t%=m
    if t==0:
        N-=1
        continue
    m=t
    heappush(A,-t)
print(cnt)