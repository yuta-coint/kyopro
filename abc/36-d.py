import sys
input = sys.stdin.readline
sys.setrecursionlimit(10 ** 6)
mod = 10**9+7
n = int(input())
G  =[[]for i in range(n)]
for i in range(n-1):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
check = [True for i in range(n)]
black = [1 for i in range(n)]
white = [1 for i in range(n)]
def dfs(v):
    check[v] = False
    for i in G[v]:
        if check[i]:
            dfs(i)
            black[v]*=white[i]
            black[v]%=mod
            white[v]*=black[i]+white[i]
            white[v]%mod
dfs(0)
#print(black)
#print(white)
print((white[0]+black[0])%mod)


