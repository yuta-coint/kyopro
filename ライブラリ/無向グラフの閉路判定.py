import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
n,m = map(int,input().split())
G = [[] for i in range(n)]
tree = [i for i in range(n)]
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
ans = "Yes"
for _ in range(m):
    a,b = map(int,input().split())
    if find(a)==find(b):
        ans="No"
        break
    else:
        union(a,b)
print(ans)