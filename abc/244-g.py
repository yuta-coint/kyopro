import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N,M = map(int,input().split())
G  =[[] for i in range(N)]
for i in range(M):
    u,v = map(lambda x:int(x)-1,input().split())
    G[u].append(v)
    G[v].append(u)
s = input()
ans = []
unvisited = [True for i in range(N)]
cnt=[0 for i in range(N)]
def dfs(v):
    unvisited[v]=False
    ans.append(v+1)
    cnt[v]=1-cnt[v]
    for i in G[v]:
        if unvisited[i]:
            dfs(i)
            ans.append(v+1)
            cnt[v]=1-cnt[v]
            if cnt[i]!=int(s[i]):
                ans.append(i+1)
                cnt[i]=1-cnt[i]
                ans.append(v+1)
                cnt[v]=1-cnt[v]
dfs(0)
#print(cnt)
if cnt[0]!=int(s[0]):
    ans.pop()
print(len(ans))
print(*ans)
