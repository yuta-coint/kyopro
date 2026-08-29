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
N,M = map(int,input().split())
G = [[0 for i in range(N)] for j in range(N)]
edges = []
for i in range(M):
    u,v = map(int,input().split())
    G[u-1][v-1] += 1
    G[v-1][u-1] += 1
#各成分の全域木を数え上げる。
#ラプラシアン行列の行列式に自由な辺の場合の数を掛ける
#連結成分がN-K個の全域木の数を数えればいい。
forest_count = [[0 for i in range(1<<N)] for k in range(N-1)]
for bits in range(1,1<<N):
    pc = 0
    pop_list = []
    for i in range(N):
        if (bits>>i)&1:
            pop_list.append(i)
            pc+=1
    if pc==1:
        forest_count[0][bits]=1
    else:
        Lap = [[0 for i in range(pc)] for j in range(pc)]
        for i in range(pc-1):
            for j in range(i+1,pc):
                pi,pj = pop_list[i],pop_list[j]
                Lap[i][j]=-G[pi][pj]
                Lap[j][i]=-G[pi][pj]
                Lap[i][i]+=G[pi][pj]
                Lap[j][j]+=G[pi][pj]
        forest_count[0][bits] = determinant(Lap,pc-1)
    t = pop_list[0]
    u = bits
    while u>0:
        if (u>>t)&1:
            for k in range(1,N-1):
                forest_count[k][bits]+=forest_count[k-1][bits-u]*forest_count[0][u]%mod
                forest_count[k][bits]%=mod
        u = (u-1)&bits
#多重辺ができた時点でアウト。それぞれの状態が実現できる確率M^k分のkのfac
root_event = 1
M_inv = pow(M,mod-2,mod)
for k in range(1,N):
    root_event*=M_inv*k%mod
    root_event%=mod
    #print(forest_count[N-1-k][(1<<N)-1])
    print(forest_count[N-1-k][(1<<N)-1]*root_event%mod)