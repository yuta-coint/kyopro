N,M,v = map(int,input().split())
v-=1
G = [{} for i in range(N)]
rG = [{} for i in range(N)]
for i in range(M):
    a,b,c = map(int,input().split())
    G[a-1][b-1]=c
    rG[b-1][a-1]=c
#有限回の操作で終わるならTrue
takahashi_turn = [False for i in range(N)]
aoki_turn = [False for i in range(N)]
from collections import deque
dq = deque()
to_takahashi_False = [len(rG[i]) for i in range(N)]
for i in range(N):
    if len(G[i])==0:
        takahashi_turn[i]=True
        aoki_turn[i]=True
        dq.append(i)
a_visited = [False for i in range(N)]
t_visited = [False for i in range(N)]
len_dq = len(dq)
#aokiのTrueに向かう頂点はTrue、takahashiのTrueにしか向かわない頂点もTrue
#aoki側にTrueができたらdqに追加する。
while len_dq>0:
    t = dq.popleft()