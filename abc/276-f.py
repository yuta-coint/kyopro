n = int(input())
#RSQ
#n:数列の長さ
BIT = [0 for i in range(n+1)]
BIT2 = [0 for i in range(n+1)]
def add(i,x):
    while i<=n:
        BIT[i]+=x
        BIT2[i]+=1
        i += (i&-i)
#xまでの和をとる
def getSum(x):
    i = x
    gs = 0
    gs2 = 0
    while i>0:
        gs+=BIT[i]
        gs2+=BIT2[i]
        i -= (i&-i)
    return (gs,gs2)
left_sum = [0 for i in range(n+1)]
A = list(map(int,input().split()))
qw = [(A[i],i+1) for i in range(n)]
qw.sort(reverse=True)
for (s,t) in qw:
    left_sum[t] = getSum(t)
    add(t,s)
mod = 998244353
ans = [0 for i in range(n+1)]
#print(left_sum)
for i in range(1,n+1):
    ans[i]=(ans[i-1]+left_sum[i][0]*2)%mod
    ans[i]+=A[i-1]*(2*i-1-left_sum[i][1]*2)%mod
    ans[i]%=mod
#print(ans)
for i in range(1,n+1):
    print(ans[i]*pow(i*i%mod,mod-2,mod)%mod)




