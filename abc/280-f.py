import sys
input = sys.stdin.readline
n,m,q = map(int,input().split())
###コピペ
#再帰のおまじないを忘れずに
#size[find(a)]でaを含む連結成分の大きさを出力
#一点に壊れている事が分かったらその連結成分ぶっ壊す
tree = [i for i in range(n)]
#size = [1 for i in range(n)]
weight = [0 for i in range(n)]
sys.setrecursionlimit(10**6)
def find(i):
    global weight
    if tree[i] == i:
        return i
    else:
        temp = find(tree[i])
        if weight[i] == 'inf' or weight[tree[i]]=='inf':
            weight[i]='inf'
        else:
            weight[i]+=weight[tree[i]]
        tree[i]= temp
        return temp

def union(a,b,w):
    if find(a) > find(b):
        a,b = b,a
        w*=-1
    #以下二行が各成分のサイズの処理
    #if find(a)!=find(b):
    #    size[find(a)],size[find(b)]=size[find(b)]+size[find(a)],size[find(b)]+size[find(a)]
    fb,fa = find(b),find(a)
    if weight[fb]=='inf' or weight[b]=='inf' or weight[a]=='inf' or weight[fa]=='inf':
        weight[fb]='inf'
    else:
        weight[fb]+=w-weight[b]+weight[a]+weight[fa]
    tree[fb] = fa
def diff(x,y):
    if find(x)==find(y):
        if weight[y]=='inf' or weight[x]=='inf':
            return('inf')
        else:
            return(weight[y]-weight[x])
    else:
        return("nan")
#aを含む連結成分を全×にする。
for _ in range(m):
    a,b,c = map(int,input().split())
    a-=1
    b-=1
    if find(a)==find(b):
        if diff(a,b) == c:
            continue
        else:
            weight[find(a)]='inf'
    union(a,b,c)
for _ in range(q):
    x,y = map(int,input().split())
    x-=1
    y-=1
    print(diff(x,y))
