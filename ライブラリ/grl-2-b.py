import sys
input = sys.stdin.readline
V,E,r = map(int,input().split())
###コピペ
#再帰のおまじないを忘れずに
tree = [i for i in range(V)]
size = [1 for i in range(V)]
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
    tree[find(b)] = find(a)
r-=1
G = [[float('inf') for i in range(V)] for j in range(V)]
#入ってくる辺で整理したもの
G1 = [[] for i in range(V)]
for i in range(E):
    v,w,s = map(int,input().split())
    v-=1
    w-=1
    G[v][w]=s
    G1[w].append((s,v))
#全域木ですか判定
flag = 0
temp = 0
for i in range(V):
    if r==i:
        continue
    t = min(G1[i])[1]
    if find(t)==find(i):
        flag = 1
    else:
        union(t,i)
    temp+=G[t][i]
