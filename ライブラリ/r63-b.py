N = int(input())
A = list(map(int,input().split()))
#st = [[-1] for i in range(N+2)]
ans = 0
from heapq import heapify,heappop,heappush
box = [N]
heapify(box)
for i in reversed(range(N)):
    heappush(box,i)
    #st[A[i]].append(i)
    cnt=1
    if A[i]==1:
        while True:
            t = heappop(box)
            if t == N:
                heappush(box,t)
                break
            if A[t]!=cnt:
                heappush(box,t)
                break
            cnt+=1
        k = heappop(box)
        ans+=k-i
        heappush(box,k)
        #print(ans)
print(ans)