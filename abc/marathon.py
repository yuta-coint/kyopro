import sys
n,m,k,r = map(int,input().split())
d = []
for i in range(n):
    dn = list(map(int,input().split()))
    d.append(dn)
G = [[] for i in range(n+1)]
rG = [[] for i in range(n+1)]
for i in range(r):
    s,t = map(int,input().split())
    G[s].append(t)
    rG[t].append(s)
exedge = [len(G[i]) for i in range(n+1)]
inedge = [len(rG[i]) for i in range(n+1)]
import heapq 
#Sは今できるタスク
S = []
heapq.heapify(S)
for i in range(1,n+1):
    if inedge[i]==0:
        heapq.heappush(S,[-exedge[i],i])
#今日やるタスク
worker = []
heapq.heapify(worker)
for i in range(1,m+1):
    heapq.heappush(worker,[0,i])
archive = [0 for i in range(m+1)]
assign = [-1 for i in range(m+1)]
day = 0
while True:
    day +=1
    ans = []
    t = 0
    for num in range(1,m+1):
        if worker == []:
            break
        i = heapq.heappop(worker)[1]
        archive[i]-=1
        if S==[]:
            break
        if assign[i]==-1:
            assign[i]=heapq.heappop(S)[1]
            t+=1
            ans.append(i)
            ans.append(assign[i])
    ans = [t]+ans
    print(*ans)
    sys.stdout.flush()
    temp = list(map(int, input().split()))
    if temp[0] == -1:
        break
    if temp[0] == 0:
        continue
    for j in range(1,temp[0]+1):
        task = assign[temp[j]]
        assign[temp[j]]=-1
        heapq.heappush(worker,[archive[temp[j]],temp[j]])
        for i in G[task]:
            inedge[i] -= 1
            if inedge[i] == 0:
                heapq.heappush(S,[-exedge[i],i])