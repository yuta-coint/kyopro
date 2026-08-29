N,K = map(int,input().split())
score = [list(map(int,input().split())) for i in range(N)]
from heapq import heapify,heappop,heappush
chance = []
for i in range(N):
    chance.append((-score[i][1],i))
heapify(chance)
ans=0
for i in range(K):
    t = heappop(chance)
    ans-=t[0]
    if t[1]>=0:
        heappush(chance,(-score[t[1]][0]+score[t[1]][1],-1))
print(ans)

