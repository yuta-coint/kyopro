import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
G = [[] for i in range(n)]
for i in range(n-1):
    a,b = map(lambda x:int(x)-1,input().split())
    G[a].append(b)
    G[b].append(a)
unvisited = [True for i in range(n)]
cnt = 0
team = [[],[]]
def dfs(v):
    unvisited[v]=False
    global cnt
    cnt = 1-cnt
    team[cnt].append(v+1)
    for i in G[v]:
        if unvisited[i]:
            dfs(i)
    cnt = 1-cnt
dfs(0)
if len(team[0])>=len(team[1]):
    print(*team[0][:n//2])
else:
    print(*team[1][:n//2])
