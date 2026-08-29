import sys
input = sys.stdin.readline
n,m = map(int,input().split())
seg = [list(map(int,input().split())) for i in range(m)]
for s in seg:
    s[1]*=-1
seg.sort()
for s in seg:
    s[1]*=-1
ans = 0
#RSQ
#n:数列の長さ
BIT = [0 for i in range(n+1)]
def add(i,x):
    while i<=n:
        BIT[i]+=x
        i += (i&-i)
#xまでの和をとる
def getSum(x):
    i = x
    gs = 0
    while i>0:
        gs+=BIT[i]
        i -= (i&-i)
    return gs
for s in seg:
    ans += getSum(s[1]-1)-getSum(s[0])
    add(s[1],1)
print(ans)
