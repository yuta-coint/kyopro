N = int(input())
P = [0] + list(map(int,input().split()))
G = [[] for i in range(N)]
for i in range(1,N):
    G[i].append(P[i] - 1)
    G[P[i] - 1].append(i)
#帰りがけの順序を作る#################################################
is_bottom = [False for i in range(N)]
def backward(n, X, i0):
    done = [0] * n
    Q = [-i0-1, i0] # 根をスタックに追加
    bw = []
    while Q:
        i = Q.pop()
        if i >= 0: # 行きがけの処理
            done[i] = 1
            bottom = True
            for a in X[i][::-1]:
                if done[a]: continue
                Q.append(~a) # 帰りがけの処理をスタックに追加
                Q.append(a) # 行きがけの処理をスタックに追加
                bottom =False
            if bottom:
                is_bottom[i]=True
        else: # 帰りがけの処理
            bw.append(~i)
    bw.pop()
    return bw

bwd = backward(N,G,0)
bwd.append(0)
##################################################################
mod = 998244353
fac = [0 for i in range(10**7)]
fac[0] = 1
for i in range(1, 10**7):
    fac[i] = i * fac[i - 1] % mod

fac_rev = [0] * (10**7)
fac_rev[-1] = pow(fac[-1], -1, mod)
for i in reversed(range(1, 10**7)):
    fac_rev[i - 1] = fac_rev[i] * i % mod
ans = 1
C = list(map(int,input().split()))
D = list(map(int,input().split()))
candy_count = [0 for i in range(N)]
for v in bwd:
    candy_count[v] += C[v]
    #print(v,candy_count[v],D[v])
    if D[v] > candy_count[v]:
        ans = 0
        break
    #ここに、candy_count[v]CD[v]を入れる。
    ans *= fac_rev[D[v]]
    ans %= mod
    for i in range(D[v]):
        ans *= candy_count[v] - i
        ans %= mod
    candy_count[v] -= D[v]
    candy_count[P[v] - 1] += candy_count[v]
    #print("ans:",ans)
print(ans)