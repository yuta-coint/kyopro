import sys
input = sys.stdin.readline
n,m = map(int,input().split())
###コピペ
#再帰のおまじないを忘れずに
#size[find(a)]でaを含む連結成分の大きさを出力
tree = [i for i in range(n)]
#size = [1 for i in range(n)]
sys.setrecursionlimit(10**6)
def find(i):
    if tree[i] == i:
        return i
    else:
        tree[i]= find(tree[i])
        return find(tree[i])

def union(a,b):
    if tree[a] > tree[b]:
        a,b = b,a
    #以下二行が各成分のサイズの処理
    #if find(a)!=find(b):
    #    size[find(a)],size[find(b)]=size[find(b)]+size[find(a)],size[find(b)]+size[find(a)]
    tree[find(b)] = find(a)

A = list(map(int,input().split()))
edges = [tuple(map(lambda x:int(x)-1,input().split())) for i in range(m)]
for u,v in edges:
    if A[u]==A[v]:
        union(u,v)
G = [[] for i in range(n)]
for u,v in edges:
    if A[u]==A[v]:
        continue
    if A[u]<A[v]:
        G[find(u)].append(find(v))
    else:
        G[find(v)].append(find(u))
score = [-10**9 for i in range(n)]
B = [(A[i],i) for i in range(n)]
B.sort()
score[find(0)]=1
for t,k in B:
    for s in G[k]:
        if score[s]<score[k]+1:
            score[s] = score[k]+1
if score[find(n-1)]<-10**8:
    print(0)
else:
    print(score[find(n-1)])