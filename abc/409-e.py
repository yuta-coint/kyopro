N=  int(input())
X = list(map(int,input().split()))
G = [[] for i in range(N)]
for i in range(N-1):
    u,v,w = map(int,input().split())
    G[u-1].append((v-1,w))
    G[v-1].append((u-1,w))
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
            for a, w in X[i][::-1]:
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
parent_weight = [-1 for i in range(N)]
for i in range(N):
    for s,w in G[i]:
        if parent[i] == s:
            parent_weight[i] = w

ans = 0
for i in bwd:
    ans+=parent_weight[i]*abs(X[i])
    X[parent[i]]+=X[i]
print(ans)