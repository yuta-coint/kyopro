import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
from collections import deque
N,M = map(int,input().split())
G=[[] for i in range(N)]
for i in range(N-1):
    x,y = map(int,input().split())
    G[x-1].append(y-1)
    G[y-1].append(x-1)
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
bwd.append(0)
#########################################################
#普通の木dp
dp = [1 for i in range(N)]
for edge in bwd:
    for son in G[edge]:
        if son == parent[edge]:
            continue
        #子の頂点の値から親の頂点を導く##
        dp[edge]*=dp[son]+1
        dp[edge]%=M
        ##############################
dp_up = [1 for i in range(N)]
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
bfs(0)
#print(dp_up)
for i in range(N):
    ans = 1
    if i==0:
        print(dp[0])
    else:
        print(dp[i]*(dp_up[i]+1)%M)

