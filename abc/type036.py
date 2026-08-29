n,Q = map(int,input().split())
import sys
input = sys.stdin.readline
points = []
maxs = -float('inf')
mins = float('inf')
maxd = -float('inf')
mind = float('inf')
for i in range(n):
    x,y = map(int,input().split())
    points.append([x+y,x-y])
    maxs = max(maxs,x+y)
    mins = min(mins,x+y)
    maxd = max(maxd,x-y)
    mind = min(mind,x-y)
for i in range(Q):
    q = int(input())-1
    print(max(maxs-points[q][0],points[q][0]-mins,maxd-points[q][1],points[q][1]-mind))