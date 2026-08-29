N = int(input())
edges = [tuple(map(int,input().split())) for i in range(N-1)]
G = [[] for i in range(N)]
for i in range(N-1):
    u,v = edges[i]
    u-=1
    v-=1
    G[u].append(v)
    G[v].append(u)
white = [1 for i in range(N)]
black = [1 for i in range(N)]
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

bwd = backward(N,G,0)
##################################################################
mod = 10**9+7
for i in bwd:
    white[parent[i]]*=(white[i]+black[i])
    white[parent[i]]%=mod
    black[parent[i]]*=white[i]
    black[parent[i]]%=mod
print((white[0]+black[0])%mod)