#要するに森の各連結成分について重心を求め、それらを破壊する作業をやればいい
import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
N = int(input())
G = [[] for i in range(N)]
for i in range(N-1):
    a,b = map(int,input().split())
    G[a-1].append(b-1)
    G[b-1].append(a-1)
#各ノードの親をとる処理############
mother = [-1 for i in range(N)]
son = [[] for i in range(N)]
visited = [False for i in range(N)]
Euler = []
def dfs_mother(v):
    visited[v] = True
    for i in G[v]:
        if visited[i]:
            continue
        mother[i]=v
        son[v].append(i)
        dfs_mother(i)
    Euler.append(v)
dfs_mother(0)
#print(Euler)
################################
#破壊された頂点
broken = [False for i in range(N)]
def dfs_size():
    for i in Euler:
        if broken[i]:
            size_of_subtree[i]=0
        if mother[i]!=-1:
            size_of_subtree[mother[i]]+=size_of_subtree[i]
ans = [-1 for i in range(N)]
#直前に潰された頂点
pro = [-1 for i in range(N)]
#logNループで収まるはず
for _ in range(len(bin(N))-2):
    size_of_subtree = [1 for i in range(N)]
    dfs_size()
    #print(size_of_subtree)
    #print(broken)
    #部分木の大きさをもとに、各連結成分の中心を求める。
    #親が壊れているなら頑張る
    for i in range(N):
        #各連結成分の根でないものは飛ばす
        if broken[i]:
            continue
        if mother[i]>-1:
            if broken[mother[i]]==False:
                continue
        centeroid = i
        while True:
            for s in son[centeroid]:
                if size_of_subtree[s]*2>size_of_subtree[i]:
                    centeroid = s
                    break
            else:
                ans[centeroid]=pro[i]
                if centeroid!=i:
                    pro[i]=centeroid
                for s in son[centeroid]:
                    pro[s]=centeroid
                broken[centeroid]=True
                break
for i in range(N):
    if ans[i]!=-1:
        ans[i]+=1
print(*ans)