import sys
input = sys.stdin.readline
#同じのを認めると座標圧縮に支障が出るので適当にずらす
N,m = map(int,input().split())
a = []
for i in range(N):
    ai = list(map(int,input().split()))
    ai.sort()
    for j in range(m):
        a.append(ai[j])
sa = sorted(a)
n = N*m
#座標圧縮
dict = {sa[i]:i+1 for i in range(n)}
a = [dict[a[i]] for i in range(n)]
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
ans = 0
#同じ値を認めない場合、getSum(a[i]-1)になる
for i in reversed(range(n)):
    ans+=getSum(a[i])
    add(a[i],1)
print(ans)
print(ans+m*(m+1)*N*(N-1)//4)