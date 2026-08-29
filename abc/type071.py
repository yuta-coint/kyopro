#トポロジカルソートする
from typing import List
N,M,K = map(int,input().split())
G = [[] for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
inedge = [0]*N
for frm in range(N):
    for to in G[frm]:
        inedge[to]+=1
L = []
from collections import deque
St = deque()
for i in range(N):
    if inedge[i]==0:
        St.append(i)
pat = 0
start = [-1 for i in range(K)]
ans = [-1 for i in range(K)]
from copy import copy
catched = [False for i in range(N)]
start[0] = [St,inedge,[]]
cnt = 1

for k in range(K):
    if start[k]==-1:
        print(-1)
        exit()
    S = start[k][0]
    ls = len(S)
    inedge = start[k][1]
    L = start[k][2]
    while S:
        if ls>1 and cnt<K:
            for i in range(1,ls):
                newS = copy(S)
                newS.remove(S[i])
                newL = copy(L)
                new_inedge = copy(inedge)
                newL.append(S[i])
                for v in G[S[i]]:
                    new_inedge[v]-=1
                    if new_inedge[v]==0:
                        newS.append(v)
                start[cnt]=[newS,new_inedge,newL]
                cnt+=1
                if cnt==K:
                    break
        n = S.popleft()
        ls -= 1
        L.append(n)
        for i in G[n]:
            inedge[i] -= 1
            if inedge[i] == 0:
                S.append(i)
                ls+=1
    if max(inedge)==0:
        ans[k]=[L[i]+1 for i in range(N)]
    else:
        print(-1)
        exit()
for k in range(K):
    print(*ans[k])

    