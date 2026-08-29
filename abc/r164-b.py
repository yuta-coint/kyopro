import sys
input = sys.stdin.readline
N,M = map(int,input().split())
G = [[] for i in range(N)]
visited = [-1 for i in range(N)]
for i in range(M):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
c = list(map(int,input().split()))
def dfs(w,time):
    S = []
    S.append(w)
    while S:
        v = S.pop()
        if visited[v]>=0:
            continue
        visited[v]=time
        for i in G[v]:
            if c[v]==c[i]:
                if visited[i]==time:
                    print("Yes")
                    exit()
            else:
                S.append(i)
for i in range(N):
    if visited[i]>=0:
        continue
    dfs(i,i)
print("No")