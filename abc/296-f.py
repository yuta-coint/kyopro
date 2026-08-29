from copy import copy
N=int(input())
A=  list(map(int,input().split()))
B =  list(map(int,input().split()))
#集合が同一か
C = copy(A)
D = copy(B)
C.sort()
D.sort()
if C!=D:
    print("No")
    exit()
#同じのが二個あるか
if len(set(A))<N:
    print("Yes")
    exit()
d = {}
for i in range(N):
    d[A[i]]=i
cnt = [0 for i in range(N)]
for i in range(N):
    cnt[d[B[i]]]=i
#同じのを認めると座標圧縮に支障が出るので適当にずらす
n = N
a = cnt
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
#同じ値を認めない場合、getSum(a[i]-1)になる
for i in reversed(range(n)):
    ans+=getSum(a[i])
    add(a[i],1)
if ans&1:
    print("No")
else:
    print("Yes")