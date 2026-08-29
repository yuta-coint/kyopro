import sys
from copy import copy
input = sys.stdin.readline
N = int(input())
tree = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    tree[a-1].append(b-1)
    tree[b-1].append(a-1)
C = list(map(int,input().split()))
#Euler tourを作る#################################################
#Cは各頂点の重み
def parent_chk(n, X, i0):
    done = [0] * n
    Q = [-i0-1, i0] # 根をスタックに追加
    p = [-1 for i in range(n)]
    while Q:
        i = Q.pop()
        if i >= 0: # 行きがけの処理
            done[i] = 1
            for a in X[i][::-1]:
                if done[a]: continue
                p[a]=i
                Q.append(a) # 行きがけの処理をスタックに追加
    return p

parent = parent_chk(N,tree,0)
##################################################################
def size_of_subtree_cnt(n, X, i0):
    r = copy(C)
    done = [0] * n
    Q = [-i0-1, i0] # 根をスタックに追加
    while Q:
        i = Q.pop()
        if i >= 0: # 行きがけの処理
            done[i] = 1
            for a in X[i][::-1]:
                if done[a]: continue
                parent[a]=i
                Q.append(~a) # 帰りがけの処理をスタックに追加
                Q.append(a) # 行きがけの処理をスタックに追加
        else: # 帰りがけの処理
            if -i-1!=0:
                r[parent[-i-1]]+=r[-i-1]
    return r
size_of_subtree = size_of_subtree_cnt(N,tree,0)
def SubFindCenteroids(X):
    ctr = []
    allw = sum(C)
    for i in range(N):
        for j in X[i]:
            if j==parent[i]:
                continue
            if size_of_subtree[j]>allw//2:
                break
        else:
            if allw-size_of_subtree[i]<=allw//2:
                ctr.append(i)
    return ctr
#################################################

def dist_from_i0(n, X, i0):
    done = [0] * n
    Q = [-i0-1, i0] # 根をスタックに追加
    dist = [0 for i in range(N)]
    while Q:
        i = Q.pop()
        if i >= 0: # 行きがけの処理
            done[i] = 1
            for a in X[i][::-1]:
                if done[a]: continue
                dist[a] = dist[i]+1
                Q.append(a) # 行きがけの処理をスタックに追加
    return dist
ans = 10**24
for cand in SubFindCenteroids(tree):
    d = dist_from_i0(N,tree,cand)
    temp = 0
    for i in range(N):
        temp+=d[i]*C[i]
    if temp<ans:
        ans = temp
print(size_of_subtree)
print(ans)
        