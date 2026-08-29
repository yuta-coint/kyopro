import sys
input = sys.stdin.readline
N,Q = map(int,input().split())
n = N+Q
###コピペ
#再帰のおまじないを忘れずに
#comp_size[find(a)]でaを含む連結成分の大きさを出力
tree = [i for i in range(n)]
comp_size = [1 for i in range(n)]
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
        comp_size[find(a)],comp_size[find(b)]=comp_size[find(b)]+comp_size[find(a)],comp_size[find(b)]+comp_size[find(a)]
    tree[find(b)] = find(a)
#異なる連結成分に属する頂点であって、距離が最小の組み合わせを持ちたい。
nodes = []
M = 0

from heapq import heapify,heappop,heappush
dist = []
heapify(dist)
def add_node(a,b):
    global M
    for i in range(M):
        heappush(dist,(abs(nodes[i][0]-a)+abs(nodes[i][1]-b),M*(10**5)+i))
    nodes.append((a,b))
    M+=1
    return
def connect():
    k = -1
    while dist:
        d,st = heappop(dist)
        s,t = st//(10**5),st%(10**5)
        if find(s)!= find(t):
            union(s,t)
            k = d
            break
    while dist:
        d,st = heappop(dist)
        if d!=k:
            heappush(dist,(d,st))
            break
        s,t = st//(10**5),st%(10**5)
        union(s,t)
    return k

for i in range(N):
    x,y = map(int,input().split())
    add_node(x,y)
#print(nodes,dist)
for _ in range(Q):
    q = list(map(int,input().split()))
    if q[0]==1:
        add_node(q[1],q[2])
    elif q[0]==2:
        print(connect())
    else:
        if find(q[1]-1) == find(q[2]-1):
            print("Yes")
        else:
            print("No")