import sys
input = sys.stdin.readline
n,m,K = map(int,input().split())
###コピペ
#再帰のおまじないを忘れずに
#size[find(a)]でaを含む連結成分の大きさを出力
tree = [i for i in range(n)]
size_A = [0 for i in range(n)]
size_B = [0 for i in range(n)]
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
    if find(a)!=find(b):
        size_A[find(a)],size_A[find(b)]=size_A[find(b)]+size_A[find(a)],size_A[find(b)]+size_A[find(a)]
        size_B[find(a)],size_B[find(b)]=size_B[find(b)]+size_B[find(a)],size_B[find(b)]+size_B[find(a)]
    tree[find(b)] = find(a)
edges = []
for i in range(m):
    u,v,w = map(int,input().split())
    edges.append((w,u-1,v-1))
A = list(map(int,input().split()))
for a in A:
    size_A[a-1]+=1
B = list(map(int,input().split()))
for b in B:
    size_B[b-1]+=1
edges.sort()
ans = 0
for i in range(m):
    w,u,v = edges[i]
    union(u,v)
    m = min(size_A[find(u)],size_B[find(u)])
    ans+=m*w
    size_A[find(u)]-=m
    size_B[find(u)]-=m
print(ans)