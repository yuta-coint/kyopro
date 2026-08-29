import sys
input = sys.stdin.readline
v,m = map(int,input().split())
graph = [list(map(int,input().split())) for i in range(m)]
tree = [i for i in range(v)]
size = [1 for i in range(v)]
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
ans = []
bad = v*(v-1)//2
for i in reversed(range(m)):
    p,q = graph[i][0]-1,graph[i][1]-1
    ans.append(bad)
    if find(p)!=find(q):
        sp = size[find(p)]
        sq = size[find(q)]
        bad+= (sp*(sp-1)+sq*(sq-1)-(sp+sq)*(sp+sq-1))//2
        size[find(p)]+=size[find(q)]
        size[find(q)]=size[find(p)]
    union(p,q)
for i in reversed(range(m)):
    print(ans[i])
