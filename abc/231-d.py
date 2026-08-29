import sys
input = sys.stdin.readline
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
for i in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    G[a].append(b)
    G[b].append(a)
    if find(a)==find(b):
        ans = "No"
    else:
        union(a,b)
for i in range(n):
    if len(G[i])>=3:
        ans="No"
print(ans)





