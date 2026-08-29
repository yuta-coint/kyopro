N,M = map(int,input().split())
if M!=N-1:
    print("No")
    exit()
import sys
input = sys.stdin.readline
n = N
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
deg = [0 for i in range(N)]
for i in range(M):
    u,v = map(int,input().split())
    union(u-1,v-1)
    deg[u-1]+=1
    deg[v-1]+=1
one = 0
for i in range(N):
    if deg[i]==1:
        one+=1
    elif deg[i]!=2:
        print("No")
        exit()
if one!=2:
    print("No")
    exit()
for i in range(N):
    if find(0)!=find(i):
        print("No")
        exit()
print("Yes")
