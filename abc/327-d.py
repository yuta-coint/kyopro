#https://prd-xxx.hateblo.jp/entry/2017/10/13/004256
# 再帰の深さが1000を超えそうなときはこれをやっておく
import sys
sys.setrecursionlimit(10**7)

# 入力のつもり。esはよくある隣接リストで辺を表したもの。
N,M = map(int,input().split())
es = [[] for i in range(N)] # True
A = list(map(int,input().split()))
B = list(map(int,input().split()))
alr = set()
big = 10**9
for i in range(M):
    if A[i]*big+B[i] in alr:
        continue
    if A[i]==B[i]:
        print("No")
        exit()
    es[A[i]-1].append(B[i]-1)
    es[B[i]-1].append(A[i]-1)
    alr.add(A[i]*big+B[i])
    alr.add(A[i]+B[i]*big)

#n個の頂点の色を初期化。0:未着色、1:黒、-1:白
colors = [0 for i in range(N)] 
visited = [False for i in range(N)]
#頂点vをcolor(1 or -1)で塗り、再帰的に矛盾がないか調べる。矛盾があればFalse
def dfs(v,color):
    #今いる点を着色
    visited[v] = True
    colors[v] = color
    #今の頂点から行けるところをチェック
    for to in es[v]:
        #同じ色が隣接してしまったらFalse
        if colors[to] == color:
            return False
        #未着色の頂点があったら反転した色を指定し、再帰的に調べる
        if colors[to] == 0 and not dfs(to, -color):
            return False
    #調べ終わったら矛盾がないのでTrue
    return True

#2部グラフならTrue, そうでなければFalse
def is_bipartite():
    for i in range(N):
        if visited[i]:
            continue
        if dfs(i,1):
            continue
        else:
            return False
    return True

if is_bipartite():
    print("Yes")
else:
    print("No")