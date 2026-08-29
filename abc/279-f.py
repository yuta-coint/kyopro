N,Q = map(int,input().split())

import sys
input = sys.stdin.readline
n = N+Q+3
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
    #if find(a)!=find(b):
    #    size[find(a)],size[find(b)]=size[find(b)]+size[find(a)],size[find(b)]+size[find(a)]
    tree[find(b)] = find(a)
k = N
#最終的にいる箱
parents = [i for i in range(N+1)]
#どの箱がどのノードに所属しているかそれとも空か
newboxs = [i for i in range(N+1)]
node_to_no = [i for i in range(N+1)]+[-1 for i in range(Q+1)]
for _ in range(Q):
    op = list(map(int,input().split()))
    if op[0]==1:
        x,y = op[1],op[2]
        if newboxs[y]==0:
            continue
        #xが空箱→xに対応するノードを
        if newboxs[x]==0:
            newboxs[x]=newboxs[y]
            node_to_no[find(newboxs[x])]=x
            newboxs[y]=0
        #xが空でない→xに対応するノードをfind(x)に変える
        else:
            union(newboxs[x],newboxs[y])
            newboxs[x]=find(newboxs[x])
            node_to_no[find(newboxs[x])]=x
            newboxs[y]=0
    elif op[0]==2:
        k+=1
        if newboxs[x]==0:
            newboxs[x]=k
            node_to_no[k]=x
        else:
            union(newboxs[x],k)
            node_to_no[find(k)]=newboxs[x]
    else:
        #ボールがどのノードに属しているか→箱番号に変換
        x = op[1]
        node = find(x)
        print(node_to_no[node])
    #print(newboxs)
    #print(node_to_no)

