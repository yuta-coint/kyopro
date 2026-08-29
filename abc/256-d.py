import sys
input = sys.stdin.readline
N = int(input())
areas = []
for i in range(N):
    l,r = map(int,input().split())
    areas.append((l,r))
areas.sort()
cnt = 0
L = areas[0][0]
R = areas[0][1]
ans = []
for i in range(N):
    if areas[i][0]<=R:
        R = max(R,areas[i][1])
    else:
        ans.append((L,R))
        L=areas[i][0]
        R=areas[i][1]
ans.append((L,R))
for a in ans:
    print(*a)