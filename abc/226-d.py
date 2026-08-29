N = int(input())
magics = set()
city = []
from math import gcd
for i in range(N):
    x,y = map(int,input().split())
    city.append((x,y))
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        dx,dy = city[j][0]-city[i][0],city[j][1]-city[i][1]
        g = gcd(dx,dy)
        if (dx//g,dy//g) not in magics:
            magics.add((dx//g,dy//g))
print(len(magics))