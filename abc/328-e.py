N,M,K = map(int,input().split())
edges = [tuple(map(int,input().split())) for i in range(M)]
import sys
input = sys.stdin.readline
###コピペ
#再帰のおまじないを忘れずに
#size[find(a)]でaを含む連結成分の大きさを出力
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
    #以下二行が各成分のサイズの処
    tree[find(b)] = find(a)

from itertools import combinations
ans = K
for t in combinations(edges,N-1):
    used = [0 for i in range(N)]
    tree = [i for i in range(N)]
    cost=0
    for i in range(N-1):
        union(t[i][0]-1,t[i][1]-1)
        cost += t[i][2]
        cost %= K
    for i in range(N):
        if find(i)!=find(0):
            break
    else:
        if cost<ans:
            ans = cost
print(ans)