N = int(input())
products = [tuple(map(int,input().split())) for i in range(N)]
products.sort()
from heapq import heappush, heappop
hq = []
time = 0
cnt = 0
#次の賞品を入れるまでにできるだけ印字しておく
ans = 0
for i in range(N):
    while time<products[i][0]:
        if cnt == 0:
            break
        end = heappop(hq)
        cnt-=1
        if end>=time:
            ans+=1
            time+=1
    time = products[i][0]
    heappush(hq,products[i][1]+products[i][0])
    cnt +=1
    #print(ans)
while cnt>0:
    end = heappop(hq)
    cnt-=1
    if end >= time:
        ans+=1
        time+=1
print(ans)