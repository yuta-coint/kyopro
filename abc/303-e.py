N = int(input())
G = [[] for i in range(N)]
deg = [0 for i in range(N)]
for i in range(N-1):
    u,v = map(int,input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)
    deg[u-1]+=1
    deg[v-1]+=1
#from collections import deque
#mnl = deque()
mnl = []
for i in range(N):
    if deg[i]==1:
        mnl.append(i)
ans = []
while mnl:
    ed = mnl.pop()
    if deg[ed]==0:
        continue
    for c in G[ed]:
        if deg[c]>0:
            center = c
            break
    #星を消しつつ答えに追加
    ans.append(deg[center])
    deg[center]=0
    for leaf in G[center]:
        if deg[leaf]>0:
            for chk in G[leaf]:
                if deg[chk]>0:
                    deg[chk]-=1
                    if deg[chk]==1:
                        mnl.append(chk)
            deg[leaf]=0
ans.sort()
print(*ans)