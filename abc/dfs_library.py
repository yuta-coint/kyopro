N = int(input())
edges = [tuple(map(int,input().split())) for i in range(N-1)]
G = [[] for i in range(N)]
for i in range(N-1):
    u,v,w = edges[i]
    u-=1
    v-=1
    G[u].append(v)
    G[v].append(u)
#Euler tourを作る#################################################
parent = [-1 for i in range(N)]

def EulerTour(n, X, i0):
    done = [0] * n
    Q = [-i0-1, i0] # 根をスタックに追加
    ET = []
    while Q:
        i = Q.pop()
        if i >= 0: # 行きがけの処理
            done[i] = 1
            ET.append(i)
            for a in X[i][::-1]:
                if done[a]: continue
                parent[a]=i
                Q.append(~i) # 帰りがけの処理をスタックに追加
                Q.append(a) # 行きがけの処理をスタックに追加

        else: # 帰りがけの処理
            ET.append(-i-1)
    ET.pop()
    return ET

Euler = EulerTour(N,G,0)
len_Euler = len(Euler)
##################################################################
#Euler tourを作る#################################################
parent = [-1 for i in range(N)]

def EulerTour(n, X, i0):
    done = [0] * n
    Q = [-i0-1, i0] # 根をスタックに追加
    ET = []
    while Q:
        i = Q.pop()
        if i >= 0: # 行きがけの処理
            done[i] = 1
            ET.append(i)
            for a in X[i][::-1]:
                if done[a]: continue
                parent[a]=i
                Q.append(~i) # 帰りがけの処理をスタックに追加
                Q.append(a) # 行きがけの処理をスタックに追加

        else: # 帰りがけの処理
            ET.append(-i-1)
    ET.pop()
    return ET

Euler = EulerTour(N,G,0)
len_Euler = len(Euler)
##################################################################