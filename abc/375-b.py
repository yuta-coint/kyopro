from math import sqrt
def dist(p,q):
    a,b,c,d = p[0],p[1],q[0],q[1]
    return sqrt((a-c)**2+(b-d)**2)
now = (0,0)
N = int(input())
ans = 0
for i in range(N):
    R = tuple(map(int,input().split()))
    ans += dist(now,R)
    now = R
ans+=dist(now,(0,0))
print(ans)