#ベルマンフォード
import sys
input = sys.stdin.readline
v,e = map(int,input().split())
edge = []
for i in range(e):
    s,t,d = map(lambda x:int(x)-1,input().split())
    edge.append([s,t,-d-1])
length = ["INF" for i in range(v)]
length[0] = 0
for i in range(v-1):
    for j in edge:
        if length[j[0]] != "INF":
            if length[j[1]] == "INF":
                length[j[1]] = length[j[0]] + j[2]
            elif length[j[1]] > length[j[0]] + j[2]:
                length[j[1]] = length[j[0]] + j[2]
ans = length[v-1]
for i in range(v-1):
    for j in edge:
        if length[j[0]] != "INF":
            if length[j[1]] == "INF":
                length[j[1]] = length[j[0]] + j[2]
            elif length[j[1]] > length[j[0]] + j[2]:
                length[j[1]] = length[j[0]] + j[2]
if ans != length[v-1]:
    print("inf")
else:
    print(-ans)
