from heapq import heappush, heappop
import sys
input = sys.stdin.readline
v, e = map(int,input().split())
length = [["INF" for i in range(v)] for j in range(v)]
G = []
for i in range(v):
    length[i][i]=0
for i in range(e):
    a,b,c = map(int,input().split())
    if a==1:
        G.append([b-1,c])
    elif b==1:
        G.append([a-1,c])
    else:
        length[a-1][b-1] = c
        length[b-1][a-1] = c
for i in range(v):
     for j in range(v):
         for k in range(v):
             if length[j][i]!="INF" and length[i][k]!="INF":
                 if length[j][k] == "INF":
                     length[j][k]=length[j][i]+length[i][k]
                 elif length[j][k]>length[j][i]+length[i][k]:
                     length[j][k]=length[j][i]+length[i][k]

k = len(G)
ans = float("inf")
for i in range(k-1):
    for j in range(i+1,k):
        if length[G[i][0]][G[j][0]]!="INF":
            temp = G[i][1]+G[j][1]+length[G[i][0]][G[j][0]]
            if temp<ans:
                ans = temp
if ans == float("inf"):
    print(-1)
else:
    print(ans)
       