N,M = map(int,input().split())
n = N
import sys
tree = [i for i in range(n)]
size = [1 for i in range(n)]
sys.setrecursionlimit(10**6)
conn_comp = n
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
        conn_comp -= 1
        size[find(a)],size[find(b)]=size[find(b)]+size[find(a)],size[find(b)]+size[find(a)]
    tree[find(b)] = find(a)
#関わっている頂点を数え、全て消したとき、
G = [[] for i in range(N)]
kata = [[] for i in range(N)]
for i in range(M):
    u,v = map(lambda x:int(x)-1,input().split())
    G[u].append(v)
    G[v].append(u)
kanren = set()
ans = 0
for i in range(N):
    if not(i in kanren):
        ans+=1
        kanren.add(i)
    for v in G[i]:
        if not(v in kanren):
            ans += 1
            kanren.add(v)
        if v<i:
            union(v,i)
    if size[find(0)]!=i+1:
        print(-1)
    else:
        print(ans-i-1)