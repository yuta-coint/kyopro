import sys
input = sys.stdin.readline
n,d = map(int,input().split())
wall = []
ll = []
lr = []
for i in range(n):
    l,r = map(int,input().split())
    wall.append([r,l])
wall.sort()
ans = 1
broken = wall[0][0]+d-1
for i in range(1,n):
    if broken>=wall[i][1]:
        continue
    ans+=1
    broken = wall[i][0]+d-1
print(ans)
