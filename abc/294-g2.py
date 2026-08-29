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
range_Euler = [[len_Euler+1,0] for i in range(N)]
for i in range(len_Euler):
    if range_Euler[Euler[i]][0]>i:
        range_Euler[Euler[i]][0]=i
    if range_Euler[Euler[i]][1]<i:
        range_Euler[Euler[i]][1]=i
#print(range_Euler)
#セグ木を作る
#RSQ
n=len_Euler
#n:数列の長さ
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
def RQT_add(u,w):
    add(range_Euler[u][0],w)
    add(range_Euler[u][1]+1,-w)
def RQT_getSum(u):
    return(getSum(range_Euler[u][0]))
##########################################################
n1 = N
logn = len(bin(n1))-1
#iの2**j個先の親を求める。何もない場合は-1を出力する
mother = [[-1 for i in range(n1+1)] for j in range(logn)]
depth = [-1 for i in range(n1)]
d = 0
cnt = 0
stack = [0]
depth[0]=0
while stack:
    v = stack.pop()
    #ord[v] = cnt
    #cnt+=1
    for i in G[v]:
        if depth[i]==-1:
            depth[i] = depth[v]+1
            mother[0][i]=v
            stack.append(i)
for i in range(1,logn):
    for j in range(n1):
        mother[i][j]=mother[i-1][mother[i-1][j]]
def LCA(u,v):
    if depth[u]>depth[v]:
        u,v = v,u
    gap = depth[v]-depth[u]
    f = 0
    while gap>0:
        if gap&1:
            v = mother[f][v]
        gap>>=1
        f+=1
    for i in reversed(range(logn)):
        if mother[i][u]!=mother[i][v]:
            u = mother[i][u]
            v = mother[i][v]
    if u == v:
        return(u)
    else:
        return(mother[0][u])
##########################################################
check = [-1 for i in range(N)]
for i in range(N-1):
    u,v,w = edges[i]
    u-=1
    v-=1
    if parent[u]==v:
        #print(u,w)
        RQT_add(u,w)
        check[i]=u
    else:
        #print(v,w)
        RQT_add(v,w)
        check[i]=v
#print(check)
#print(RQT_getSum(0))
Q = int(input())
weight = [edges[i][2] for i in range(N-1)]
for i in range(Q):
    ty,e,p = map(int,input().split())
    if ty==1:
        RQT_add(check[e-1],-weight[e-1])
        RQT_add(check[e-1],p)
        weight[e-1]=p
    else:
        ans = RQT_getSum(e-1)+RQT_getSum(p-1)
        s = LCA(e-1,p-1)
        #print(s)
        ans-=RQT_getSum(s)*2
        print(ans)
