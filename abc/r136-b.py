n=int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
sa = sorted(a)
sb = sorted(b)
p = "N"
for i in range(n-1):
    if sa[i]==sa[i+1]:
        p = "Yes"
for i in range(n):
    if sa[i]!=sb[i]:
        p = "No"
#同じのを認めると座標圧縮に支障が出るので適当にずらす
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
ans1 = 0
#同じ値を認めない場合、getSum(a[i]-1)になる
for i in reversed(range(n)):
    ans1+=getSum(a[i])
    add(a[i],1)
#n:数列の長さ
dict2 = {sb[i]:i+1 for i in range(n)}
b = [dict2[b[i]] for i in range(n)]
BIT = [0 for i in range(n+1)]
ans2 = 0
#同じ値を認めない場合、getSum(a[i]-1)になる
for i in reversed(range(n)):
    ans2+=getSum(b[i])
    add(b[i],1)
if p=="N":
    if (ans1-ans2)%2==0:
        p = "Yes"
    else:
        p = "No"
print(p)
