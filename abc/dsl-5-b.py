import sys
input = sys.stdin.readline
n = int(input())
xy = [[0 for i in range(1001)] for j in range(1001)]
for i in range(n):
    x1,y1,x2,y2 = map(int,input().split())
    xy[x2][y2]+=1
    xy[x1][y2]-=1
    xy[x2][y1]-=1
    xy[x1][y1]+=1
for i in range(1000):
    for j in range(1001):
        xy[i+1][j]+=xy[i][j]
for i in range(1001):
    for j in range(1000):
        xy[i][j+1]+=xy[i][j]
m = [max(xy[i]) for i in range(1001)]
print(max(m))