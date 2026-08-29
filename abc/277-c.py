N = int(input())
import sys
input = sys.stdin.readline
n=2*N+1
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

points = [tuple(map(int,input().split())) for i in range(N)]
all = [1]+[points[i][0] for i in range(N)]+[points[i][1] for i in range(N)]
b = sorted(set(all))
d = {v:i for i, v in enumerate(b)}
for ax,bx in points:
    union(d[ax],d[bx])
ans = 1
for p in b:
    if find(d[1])==find(d[p]):
        if ans <p:
            ans=p
print(ans)
