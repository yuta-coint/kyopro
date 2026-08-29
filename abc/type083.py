N,M = map(int,input().split())
G = [set() for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    G[a-1].add(b-1)
    G[b-1].add(a-1)
Q = int(input())
hub = set()
sq = 450
for i in range(N):
    if len(G[i])>sq:
        hub.add(i)
#hubに入っている頂点を指定したとき、周りのhubに入っている頂点を調べて色を更新する
#hubに入っていない頂点を指定したとき、周りのhubに入っている頂点を調べて色を更新したのちに逐一拡散する。
color = [1 for i in range(N)]
#最終更新時間
time = [-1 for i in range(N)]
reserve = [0 for i in range(N)]
#hubが操作された時間
reserve_time = [-1 for i in range(N)]
for t in range(Q):
    x,y = map(int,input().split())
    x-=1
    for i in hub:
        if i in G[x]:
            if time[x]<reserve_time[i]:
                color[x],time[x]=reserve[i],reserve_time[i]
    print(color[x])
    color[x]=y
    reserve[x]=y
    time[x]=t
    reserve_time[x]=t
    if x in hub:
        continue
    for i in G[x]:
        color[i],time[i] = color[x],t