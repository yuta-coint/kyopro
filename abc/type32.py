from sys import implementation


import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n = int(input())
a = [list(map(int,input().split())) for i in range(n)]
m = int(input())
relation = [[1 for j in range(n)] for i in range(n)]
for i in range(m):
    x,y = map(lambda x:int(x)-1,input().split())
    relation[x][y] = 0
    relation[y][x] = 0
def ekiden(s,time):
    global ans
    L = len(s)
    if L==n:
        ans = min(ans,time)
    elif L==0:
        for i in range(n):
            ekiden(s+[i],time+a[i][L])
    else:
        for i in range(n):
            if i not in s and relation[i][s[-1]]==1:
                ekiden(s+[i],time+a[i][L])
ans = float("inf")
ekiden([],0)
if ans == float("inf"):
    print(-1)
else:
    print(ans)