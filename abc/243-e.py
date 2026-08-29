import sys
input = sys.stdin.readline
v, e = map(int,input().split())
#length[i][j]はiからjへの長さ。有向グラフを前提に書かれている
length = [["INF" for i in range(v)] for j in range(v)]
rin = [[False for i in range(v)] for j in range(v)]
G = [[]for i in range(v)]
edges = []
for i in range(v):
    length[i][i]=0
for i in range(e):
    a,b,c = map(int,input().split())
    a-=1
    b-=1
    edges.append([a,b,c])
    length[a][b] = c
    length[b][a] = c
    rin[a][b]=True
    rin[b][a]=True
ans = 0
for i in range(v):
     for j in range(v):
         for k in range(v):
             if i==j or j==k or k==i:
                 continue
             if length[j][i]!="INF" and length[i][k]!="INF":
                 if length[j][k] == "INF":
                     length[j][k]=length[j][i]+length[i][k]
                 elif length[j][k]>=length[j][i]+length[i][k]:
                     length[j][k]=length[j][i]+length[i][k]
                     if rin[j][k]:
                         ans+=1
                         rin[j][k]=False
                         rin[k][j]=False
print(ans)
