import sys
input = sys.stdin.readline
n = int(input())+1
q = int(input())
###コピペ
#再帰のおまじないを忘れずに
#size[find(a)]でaを含む連結成分の大きさを出力
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
        weight[i]+=weight[tree[i]]
        tree[i]= temp
        return temp
#bはaよりw大きい
def union(a,b,w):
    if find(a) > find(b):
        a,b = b,a
        w*=-1
    #以下二行が各成分のサイズの処理
    #if find(a)!=find(b):
    #    size[find(a)],size[find(b)]=size[find(b)]+size[find(a)],size[find(b)]+size[find(a)]
    fb,fa = find(b),find(a)
    weight[fb]+=w-weight[b]+weight[a]+weight[fa]
    tree[fb] = fa
def diff(x,y):
    if find(x)==find(y):
        return(weight[y]-weight[x])
    else:
        return("?")
#奇数項目を全てマイナス一倍する
for i in range(q):
    T,X,Y,V = map(int,input().split())
    if T==0:
        if X&1:
            union(X,Y,V)
        else:
            union(Y,X,V)
        #print(diff(1,2),diff(2,3),diff(3,4))
    else:
        temp = diff(X,Y)
        if temp=="?":
            print("Ambiguous")
        else:
            if X&1:
                V=-V
            if Y&1:
                print(-temp-V)
            else:
                print(temp+V)