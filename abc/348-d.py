#各点から各点について到達可能か考える。
from collections import deque
H,W = map(int,input().split())
A = ["#" for i in range(W+2)]+[["#"]+list(map(int,input().split()))+["#"] for i in range(H)]+["#" for i in range(W+2)]
#sからの距離を求める。
N= int(input())
med = [tuple(map(int,input().split())) for i in range(N)]
med_dict = {}
for r,c,e in med:
    med_dict[r*(W+2)+c] = e
def grid_distance(s):
    power = [0 for i in range((H+2)*(W+2))]
    visited = [0 for i in range((H+2)*(W+2))]
    visited[s]=1
    q=deque()
    q.append(s)
    while q!=[]:
        v =  q.popleft()
        tonari = [v+1,v-1,v+(W+2),v-(W+2)]
        for i in tonari:
            if visited[i]==1:
                continue
            visited[i]=1
            dist[v] = dist[v]+1
            q.append(i)
               