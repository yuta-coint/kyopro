N,M = map(int,input().split())
A = list(map(int,input().split()))
v,e = N,N*(N+1)//2
graph = []
for i in range(N-1):
    for j in range(i+1,N):
        w = (pow(A[i],A[j],M)+pow(A[j],A[i],M))%M
        graph.append((-w,i,j))

tree = [i for i in range(v)]

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

graph.sort()
#print(graph)
ans = 0
for cost,edgel,edger in graph:
    #print(tree)
    if find(edgel)!=find(edger):
        union(edgel,edger)
        ans += cost
    #print(ans)
print(-ans)
