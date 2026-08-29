N,M = map(int,input().split())
n = M
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
A = list(map(int,input().split()))
sA = [0]
for i in range(N):
    sA.append((A[i]+sA[-1])%M)
amari = [0 for i in range(M)]
base_sum = 0
for i in range(N+1):
    add(sA[i]+1,1)
    amari[sA[i]]+=1
    base_sum+=sA[i]
ans = 0
#各Mについて、差がMの二組がいくつあるかを調べる
#print(amari,sA)
for i in range(N):
    add(sA[i]+1,-1)
    amari[sA[i]]-=1
    base_sum-=sA[i]
    ans+=base_sum-getSum(M)*sA[i]+getSum(sA[i])*M
    #print(base_sum,getSum(M),sA[i],getSum(sA[i]))
print(ans)