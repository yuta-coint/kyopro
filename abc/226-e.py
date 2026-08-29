import sys
input = sys.stdin.readline
N,M=map(int,input().split())
n=N
###コピペ
#再帰のおまじないを忘れずに
tree = [i for i in range(n)]
size = [0 for i in range(n)]
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
    #print(find(a),find(b))
    if find(a)!=find(b):
        size[find(a)],size[find(b)]=size[find(b)]+size[find(a)],size[find(b)]+size[find(a)]
    else:
        size[find(a)]+=1
    tree[find(b)] = find(a)

mod = 998244353
for i in range(M):
    u,v = map(lambda x:int(x)-1,input().split())
    union(u,v)
chk = set()
for i in range(N):
    chk.add(find(i))
    #print(i,find(i))
    if size[find(i)]!=1:
        print(0)
        break
else:
    print(pow(2,len(chk),mod))