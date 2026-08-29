N,M  =map(int,input().split())
visited = [False for i in range(N+1)]
visited[1]=True
#これ以上行き先がないなら
mother = [-1 for i in range(N+1)]
cnt = [1 for i in range(N+1)]
G = [-1 for i in range(N+1)]
import sys
ssf = sys.stdout.flush
now = 1
while True:
    kv = list(input().split())
    if kv[0]=="OK":
        break
    k = int(kv[0])
    for i in range(1,k+1):
        kv[i]=int(kv[i])
    for i in range(1,k+1):
        if visited[kv[i]]==True:
            continue
        mother[kv[i]] = now
        print(kv[i])
        now = kv[i]
        break
    else:
        print(mother[now])
        now = mother[now]
    visited[now] = True
    ssf()