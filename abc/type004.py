import sys
input = sys.stdin.readline
h,w = map(int,input().split())
a = [list(map(int,input().split())) for i in range(h)]
file = [0 for i in range(h)]
rank = [0 for i in range(w)]
ans = [[0 for j in range(w)] for i in range(h)]
for i in range(h):
    for j in range(w):
        rank[j]+=a[i][j]
        file[i]+=a[i][j]
for i in range(h):
    for j in range(w):
        ans[i][j]=file[i]+rank[j]-a[i][j]
for i in range(h):
    print(*ans[i])