#mod998244353で掃き出す
mod = 998244353
def Gaussian_elimination(mat,N,M):
    #N行M列の行列matに掃き出し法を施し、
    #変形後の行列、0でない数が出ている列の一覧,0でない数が一つだけある列の数を返す
    completed = 0
    one_column = []
    for j in range(M):
        all_zero = True
        #全ゼロだったら掃きださなくて楽なのにな
        for i in range(completed,N):
            if mat[i][j]!=0:
                all_zero=False
                top = i
                break
        if all_zero:
            continue
        #非零を引っ張り上げる
        mat[completed],mat[top]=mat[top],mat[completed]
        one_column.append(j)
        #1を全消し!!
        for i in range(N):
            if i==completed:
                continue
            if mat[i][j]!=0:
                alpha = (-mat[i][j])*pow(mat[completed][j],mod-2,mod)%mod
                for t in range(M):
                    mat[i][t]+=mat[completed][t]*alpha%mod
                    if mat[i][t]>=mod:
                        mat[i][t]-=mod
        completed+=1
        if completed==N:
            break
    return(mat,one_column,completed)
def determinant(sqmat,N):
    m,o,c = Gaussian_elimination(sqmat,N,N)
    r = 1
    for i in range(N):
        r*=m[i][i]
        r%=mod
    return r
fac = [1]
for i in range(1,2*(10**7)):
    fac.append(fac[-1]*i%mod)

fac_rev = [pow(fac[-1],-1,mod)]
for i in reversed(range(1,2*(10**7))):
    fac_rev.append(fac_rev[-1]*i%mod)
fac_rev.reverse()
#print(fac_rev[:5])
X = list(map(int,input().split()))
in_deg = [0 for i in range(8)]
out_deg = [0 for i in range(8)]
Laplacian = [[0 for j in range(8)] for i in range(8)]
self_loop_0 = 0
self_loop_15 = 0
div = 1
for i in range(16):
    if i == 0:
        self_loop_0 += X[i]
        continue
    elif i == 15:
        self_loop_15 += X[i]
        continue
    out_deg[i//2] += X[i]
    in_deg[i%8] += X[i]
    Laplacian[i//2][i%8] -= X[i]
    Laplacian[i//2][i//2] += X[i]
    div *= fac_rev[X[i]]
    div %= mod
ans = 0
for s in range(8):
    for g in range(8):
        in_deg[s] += 1
        out_deg[g] += 1
        Laplacian[g][g] += 1
        flag = True
        for i in range(8):
            if in_deg[i] != out_deg[i]:
                flag = False
        #孤立成分以外が連結かどうかを判定
        visited = [False for _ in range(8)]
        def dfs(v):
            visited[v] = True
            for u in range(8):
                # 既存の無向辺
                if (Laplacian[v][u] < 0 or Laplacian[u][v] < 0) and not visited[u]:
                    dfs(u)
            # 追加した無向1本 g–s を表現
            if v == s and not visited[g]:
                dfs(g)
            if v == g and not visited[s]:
                dfs(s)
        for i in range(8):
            if in_deg[i] != 0 or out_deg[i] != 0:
                dfs(i)
                break
        for i in range(8):
            if (in_deg[i] != 0 or out_deg[i] != 0 or (i == 0 and self_loop_0 > 0) or (i == 7 and self_loop_15 > 0)) and not visited[i]:
                flag = False
        if flag:
            #print(s,g)
            #残る行を調べる
            survive = []
            for i in range(8):
                for k in range(8):
                    if Laplacian[i][k] != 0 or Laplacian[k][i] != 0:
                        survive.append(i)
                        break
            L = len(survive)
            Lap_survive = [[Laplacian[survive[i]][survive[j]] for j in range(L)] for i in range(L)]
            temp = determinant(Lap_survive,L)
            for i in range(8):
                if out_deg[i] == 0:
                    continue
                temp *= fac[out_deg[i] - 1]
                temp %= mod
            if out_deg[0] != 0:
                temp *= fac[self_loop_0 + out_deg[0] - 1] * fac_rev[self_loop_0] %mod  * fac_rev[out_deg[0] - 1] % mod
                temp %= mod
            if out_deg[7] != 0:
                temp *= fac[self_loop_15 + out_deg[7] - 1] * fac_rev[self_loop_15] % mod * fac_rev[out_deg[7] - 1] % mod
                temp %= mod
            temp *= div
            temp %= mod
            ans += temp
            ans %= mod
        in_deg[s] -= 1
        out_deg[g] -= 1
        Laplacian[g][g] -= 1
print(ans)