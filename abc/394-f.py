#次数4の頂点だけからなる部分グラフを取ってきて、
N= int(input())
n=N
import sys
tree = [i for i in range(n)]
size = [1 for i in range(n)]
sys.setrecursionlimit(10**6)
def find(i):
    if tree[i] == i:
        return i
    else:
        tree[i]= find(tree[i])
        return find(tree[i])

def union(a,b):
    global conn_comp
    if tree[a] > tree[b]:
        a,b = b,a
    #以下二行が各成分のサイズの処理
    if find(a)!=find(b):
        size[find(a)],size[find(b)]=size[find(b)]+size[find(a)],size[find(b)]+size[find(a)]
    tree[find(b)] = find(a)

edges = [tuple(map(int,input().split())) for i in range(N-1)]
G = [[] for i in range(N)]
deg = [0 for i in range(N)]
for a,b in edges:
    deg[a-1]+=1
    deg[b-1]+=1
if max(deg)<4:
    print(-1)
    exit()
for a,b in edges:
    if deg[a-1]>=4 and deg[b-1]>=4:
        G[a-1].append(b-1)
        G[b-1].append(a-1)
#次数4以下の部分木で最大のものを取ってきてください

#全方位
#帰りがけの順序を作る#################################################
from collections import deque
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
def bfs(v):
    check=[0 for i in range(N)]
    q = deque()
    ld = 0
    check[v]=1
    q.append(v)
    ld+=1
    while ld>0:
        v = q.popleft()
        ld-=1
        temp = []
        ind = []
        for i in G[v]:
            if check[i]==0:
                check[i]=1
                q.append(i)
                ld+=1
                temp.append((dp[i]+1)%M)
                ind.append(i)
            else:
                temp.append((dp_up[v]+1)%M)
                ind.append(-1)
        #print(temp,ind)
        len_temp = len(temp)
        temp_forward = [1]
        temp_backward = [1]
        for i in range(len_temp):
            #両端からの累積！
            temp_forward.append(temp_forward[-1]*temp[i]%M)
            temp_backward.append(temp_backward[-1]*temp[len_temp-1-i]%M)
        for i in range(len_temp):
            if ind[i]==-1:
                continue
            #マージ！
            dp_up[ind[i]] = temp_forward[i]*temp_backward[len_temp-i-1]%M
#print(dp)
comp = []
for cp in comp:
    bwd = backward(N,G,cp)
    bwd.append(cp)
    #########################################################
    #普通の木dp
    dp = [1 for i in range(N)]
    for edge in bwd:
        first,second,third = 0,0,0
        for son in G[edge]:
            if son == parent[edge]:
                continue
            #子の頂点の値から親の頂点を導く##
            if dp[son]>first:
                first,second,third = dp[son],first,second
            elif dp[son]>second:
                first,second,third = first,dp[son],second
            elif dp[son]>third:
                first,second,third = first,second,dp[son]
            ##############################
        dp[edge] = first+second+third
    dp_up = [1 for i in range(N)]
    bfs(cp)
#print(dp_up)
for i in range(N):
    ans = 1
    if i==0:
        print(dp[0])
    else:
        print(dp[i]*(dp_up[i]+1)%M)