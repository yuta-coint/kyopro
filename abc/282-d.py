import sys
sys.setrecursionlimit(10**7)
# 入力のつもり。esはよくある隣接リストで辺を表したもの。
N,M = map(int,input().split())
G = [[] for i in range(N)]
for i in range(M):
    u,v = map(int,input().split())
    G[u-1].append(v-1)
    G[v-1].append(u-1)

#n個の頂点の色を初期化。0:未着色、1:黒、-1:白
colors = [0 for i in range(N)]

#2部グラフならTrue, そうでなければFalse
def is_bipartite(t):
    black = 0
    white = 0
    stack = [(t,1)] # (頂点、色)のタプルをスタックする。最初は(頂点0, 黒(1))
    while stack:
        #スタックから最後に追加された(頂点, 色)をpop
        v,color = stack.pop()
        #今いる点を着色
        if colors[v]!=0:
            continue
        colors[v] = color
        if color==1:
            black+=1
        else:
            white+=1
        #今の頂点から行けるところをチェック
        for to in G[v]:
            #同じ色が隣接してしまったらFalse
            if colors[to] == color:
                 return (-1)
            #未着色の頂点があったら反転した色と共にスタックに積む
            if colors[to] == 0:
                 stack.append((to, -color))
    #調べ終わったら矛盾がないのでTrue
    return (black,white)
ans = (N*(N+1))//2
ans-=M
ok = 1
for i in range(N):
    if colors[i]==0:
        ib = is_bipartite(i)
        #print(i,ib)
        if ib==-1:
            ok=0
            break
        else:
            ans-=(ib[0]*(ib[0]+1))//2
            ans-=(ib[1]*(ib[1]+1))//2
print(ans*ok)