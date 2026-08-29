#RAQ
def add(i,x):
    while i<=w:
        BIT[i]+=x
        i += (i&-i)

def getSum(x):
    i = x
    gs = 0
    while i>0:
        gs+=BIT[i]
        i -= (i&-i)
    return gs

def raq(x1,x2,d):
    add(x1,d)
    add(x2+1,-d)
h,w,m = map(int,input().split())
BIT = [0 for i in range(w+1)]
rank = [w+1 for i in range(h+1)]
ra = [[] for i in range(h+1)]
under = h+1
left = w+1
import sys
input = sys.stdin.readline
for i in range(m):
    x,y= list(map(int,input().split()))
    rank[x] = min(rank[x],y)
    ra[x].append(y)
    if y == 1:
        under=min(under,x)
    if x==1:
        left=min(left,y)
for i in range(under,h+1):
    rank[i]=1
rans = 0
for i in reversed(range(h+1)):
    raq(rank[i],w,1)
    for j in ra[i]:
        t=getSum(j)
        rans+=t
        raq(j,j,-t)
for i in range(left,w+1):
    rans +=getSum(i)
print(h*w-rans)

