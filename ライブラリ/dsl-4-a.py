import sys
input = sys.stdin.readline
n = int(input())
lx = []
ly = []
point = []
for i in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    lx.append(x1)
    lx.append(x2)
    ly.append(y1)
    ly.append(y2)
    point.append([x1,x2,y1,y2])
bx = sorted(set(lx))
dx = {v:i for i, v in enumerate(bx)}
rdx = {i:v for i, v in enumerate(bx)}
by = sorted(set(ly))
dy = {v:i for i, v in enumerate(by)}
rdy = {i:v for i, v in enumerate(by)}
count = [[0 for i in range(len(dx))] for j in range(len(dy))]
for p in point:
    for i in range(dy[p[2]],dy[p[3]]):
        count[i][dx[p[0]]]+=1
        count[i][dx[p[1]]]-=1
ans=0
for i in range(len(dy)):
    for j in range(1,len(dx)):
        count[i][j]+=count[i][j-1]
for i in range(len(dy)-1):
    for j in range(len(dx)-1):
        if count[i][j]>0:
            ans+=(rdx[j+1]-rdx[j])*(rdy[i+1]-rdy[i])
print(ans)