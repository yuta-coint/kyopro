N,M = map(int,input().split())
import sys
input = sys.stdin.readline
###コピペ
#再帰のおまじないを忘れずに
#size[find(a)]でaを含む連結成分の大きさを出力
sys.setrecursionlimit(10**6)
tree = [i for i in range(N+1)]
#size = [1 for i in range(n)]
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
mod = 998244353
cnt=N
P = [-1]+list(map(int,input().split()))
ans = 0
for i in range(1,N+1):
    if i==P[i]:
        continue
    if find(i)!=find(P[i]):
        ans+=pow(M,cnt-2,mod)*((M*(M-1)//2)%mod)%mod
        ans%=mod
        union(i,P[i])
        cnt-=1
print(ans)