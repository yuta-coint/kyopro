N, K =map(int,input().split())
A = list(map(int,input().split()))
#とりあえず座標圧縮
def coordinate_compression(A):
    b = sorted(set(A))
    d ={v:i+1 for i, v in enumerate(b)}
    return list(map(lambda v:d[v],A))
A = coordinate_compression(A)
mod = 10**9+7
n = N
BIT = [0 for i in range(n+1)]
def add(i,x):
    while i<=n:
        BIT[i]+=x
        i += (i&-i)

def getSum(x):
    i = x
    gs = 0
    while i>0:
        gs+=BIT[i]
        i -= (i&-i)
    return gs
#どこまで左でバブルソートの回数がKを跨ぐものなのか
change_lim = []
inv=0
l = 0
for i in range(N):
    inv += getSum(N)-getSum(A[i])
    add(A[i],1)
    while l<i:
        #print(i,l,inv)
        if inv<=K:
            break
        inv -= getSum(A[l]-1)
        add(A[l],-1)
        l+=1
    change_lim.append(l)
#print(change_lim)
ans = [1]
ans_sum = [0,1]
#i個目までについて条件を満たす方法
for i in range(N):
    ans.append((ans_sum[i+1]-ans_sum[change_lim[i]])%mod)
    ans_sum.append((ans[-1]+ans_sum[-1])%mod)
#print(ans)
print(ans[-1])