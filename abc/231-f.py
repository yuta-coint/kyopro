import sys
input = sys.stdin.readline
n = int(input())
aa = list(map(int,input().split()))
sa = list(map(int,input().split()))
pair = []
for i in range(n):
    pair.append([aa[i],-sa[i]])
pair.sort()
a = [-pair[i][1] for i in range(n)]
a = [a[i]*n-i for i in range(n)]
sa = sorted(a)
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
for i in reversed(range(n)):
    ans+=getSum(a[i])
    add(a[i],1)
last = 0
cnt = 0
for i in pair:
    if i==last:
        cnt+=1
    else:
        last= i
        ans+=cnt*(cnt-1)//2
        cnt=1
ans+=cnt*(cnt-1)//2
print(ans+n)