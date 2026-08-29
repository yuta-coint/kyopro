import sys
input = sys.stdin.readline
n,m = map(int,input().split())
###コピペ
#再帰のおまじないを忘れずに
#size[find(a)]でaを含む連結成分の大きさを出力
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

def conn_comp_enumerate():
    chk = set()
    r = []
    for i in range(n):
        if find(i) in chk:
            continue
        r.append(i)
    return r
ans = m
for i in range(m):
    u,v = map(int,input().split())
    u-=1
    v-=1
    if find(u)!=find(v):
        ans -= 1
    union(u,v)
print(ans)    