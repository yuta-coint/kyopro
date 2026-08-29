import sys
input = sys.stdin.readline
n,m = map(int,input().split())
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
edges = [tuple(map(lambda x:int(x)-1,input().split())) for i in range(m)]
K = int(input())
x = list(map(lambda x:int(x)-1,input().split()))
for i in range(m):
    union(edges[i][0],edges[i][1])
for i in range(1,K):
    if find(edges[x[0]][0])!=find(edges[x[i]][0]):
        print("No")
        exit()
tree = [i for i in range(n)]
size = [0 for i in range(n)]
for v in x:
    size[edges[v][0]]+=1
    size[edges[v][1]]+=1
x = set(x)
for i in range(m):
    if i in x:
        continue
    union(edges[i][0],edges[i][1])
#奇数個からなる連結成分がいくつあるかが問題
con = set()
for i in range(n):
    con.add(find(i))
cnt = 0
for c in con:
    if size[c]&1:
        cnt+=1
if cnt in [0,2]:
    print("Yes")
else:
    print("No")




