import sys
input = sys.stdin.readline
n = int(input())
point = [list(map(int,input().split())) for i in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        ans = max(ans,(point[i][0]-point[j][0])**2+(point[i][1]-point[j][1])**2)
from math import sqrt
print(sqrt(ans))

k = int(input())
ans = []
l = len(bin(k))-2
for i in reversed(range(l)):
    if k>>i & 1:
        ans.append(2)
    else:
        ans.append(0)
print(*ans,sep="")