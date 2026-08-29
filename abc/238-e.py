N,Q = map(int,input().split())
graph = []
tree = [i for i in range(N+1)]
import sys
input = sys.stdin.readline
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
    tree[find(b)] = find(a)
for i in range(Q):
    l,r = map(int,input().split())
    union(l-1,r)
if find(0)==find(N):
    print("Yes")
else:
    print("No")