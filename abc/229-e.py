import sys
input = sys.stdin.readline
n,m = map(int,input().split())
G = [[] for i in range(n)]
for i in range(m):
    a,b = map(int,input().split())
    a-=1
    b-=1
    if a>b:
        a,b = b,a
    G[a].append(b)
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
ans = n
ansl = []
for i in reversed(range(n)):
    ansl.append(ans-i-1)
    for v in G[i]:
        if find(v)==find(i):
            continue
        else:
            union(v,i)
            ans-=1
for i in reversed(range(n)):
    print(ansl[i])