import sys
input = sys.stdin.readline
mod=998244353
N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
#帰りがけの順序を作る#################################################
parent = [-1 for i in range(N)]
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
                parent[a]=i
                Q.append(~a) # 帰りがけの処理をスタックに追加
                Q.append(a) # 行きがけの処理をスタックに追加
                bottom =False
            if bottom:
                is_bottom[i]=True
        else: # 帰りがけの処理
            bw.append(~i)
    bw.pop()
    return bw
##############################################
Euler = backward(N,G,0)
ans_white = [[0 for j in range(N+1)] for i in range(N)]
ans_black = [[0 for j in range(N+1)] for i in range(N)]
for i in range(N):
    ans_black[i][1]=1
    ans_white[i][0]=1
#各頂点について考察する
#白…それぞれの子についてans_white,ans_blackの合計をマージしていく
#部分木の大きさを計測
tree_size = [1 for i in range(N)]
for v in Euler:
    #parent[v]のans_whiteにぶち込んでいく
    new_white = [0 for i in range(tree_size[v]+tree_size[parent[v]]+1)]
    for i in range(tree_size[v]+1):
        for j in range(tree_size[parent[v]]+1):
            new_white[i+j]+=(ans_white[v][i]+ans_black[v][i])%mod*ans_white[parent[v]][j]%mod
            new_white[i+j]%=mod
    new_black = [0 for i in range(tree_size[v]+tree_size[parent[v]]+1)]
    for i in range(tree_size[v]+1):
        for j in range(tree_size[parent[v]]+1):
            #黒の回収
            new_black[i+j]+=ans_black[parent[v]][j]*ans_white[v][i]%mod
            new_black[i+j]%=mod
            if i==0 and j==0:
                continue
            new_black[i+j-1]+=ans_black[parent[v]][j]*ans_black[v][i]%mod
            new_black[i+j-1]%=mod
    tree_size[parent[v]]+=tree_size[v]
    for i in range(tree_size[parent[v]]+1):
        ans_black[parent[v]][i]=new_black[i]
        ans_white[parent[v]][i]=new_white[i]
for i in range(N):
    print((ans_white[0][i+1]+ans_black[0][i+1])%mod)