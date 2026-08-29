#1を削除するには周りの頂点のうち、
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())
G =[[] for i in range(N)]
for i in range(N-1):
    u,v = map(int,input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)
S = [0]
unvisited = [True for i in range(N)]
subtree_size = [1 for i in range(N)]
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
for v in bwd:
    subtree_size[parent[v]]+=subtree_size[v]

ans = N
for v in G[0]:
    if ans>N-subtree_size[v]:
        ans = N-subtree_size[v]
print(ans)