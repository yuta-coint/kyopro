from heapq import heappush, heappop
v, k = map(int,input().split())
#length[i][j]はiからjへの長さ。有向グラフを前提に書かれている
length = [["INF" for i in range(v)] for j in range(v)]
G = [[]for i in range(v)]
A = [list(map(int,input().split())) for i in range(v)]
for i in range(v):
    for j in range(v):
        if i==j:
            length[i][j]=0
            continue
        if A[i][j]==1:
            length[i][j]=1
for i in range(v):
     for j in range(v):
         for k in range(v):
             if length[j][i]!="INF" and length[i][k]!="INF":
                 if length[j][k] == "INF":
                     length[j][k]=length[j][i]+length[i][k]
                 elif length[j][k]>length[j][i]+length[i][k]:
                     length[j][k]=length[j][i]+length[i][k]
Q = int(input())
for q in range(Q):
    s,t = map(int,input().split())
    s-=1
    t-=1
    if length[s%v][t%v]=="INF":
        print(-1)
        continue
    if length[s%v][t%v]>0:
        print(length[s%v][t%v])
        continue
    if s%v==t%v:
        if A[s%v][t%v]==1:
            print(1)
        else:
            ans = float("inf")
            for i in range(v):
                if A[i][s%v]==1:
                    temp = length[s%v][i]
                    if temp=="INF":
                        continue
                    if temp+1<ans:
                        ans = temp+1
            if ans==float("inf"):
                print(-1)
            else:
                print(ans)
