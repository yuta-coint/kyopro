N = int(input())
p = [-1,-1]+list(map(int,input().split()))
Q = int(input())
import sys
input = sys.stdin.readline
n = N+1
###コピペ
#再帰のおまじないを忘れずに
#size[find(a)]でaを含む連結成分の大きさを出力
tree = [i for i in range(n)]
size = [1 for i in range(n)]
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
        size[find(a)],size[find(b)]=size[find(b)]+size[find(a)],size[find(b)]+size[find(a)]
    tree[find(b)] = find(a)
for _ in range(Q):
    query = list(map(int,input().split()))
    if query[0]==1:
        u,v = query[1],query[2]
        #uとvが同じグループに入る
        v = find(v)
        u = find(u)
        while u>v:
            union(u,v)
            if u == find(p[u]):
                break
            u = find(p[u])
    else:
        x = query[1]
        print(find(x))