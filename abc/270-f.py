N,M = map(int,input().split())
v = N+2
graph = []
tree = [i for i in range(v)]
X = list(map(int,input().split()))
Y = list(map(int,input().split()))
for i in range(N):
    graph.append((X[i],0,1+i))
    graph.append((Y[i],N+1,1+i))
for i in range(M):
    a,b,z = map(int,input().split())
    graph.append((z,a,b))
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
final_ans = 0
ans = 0
for i,j,k in (graph):
    #print(tree)
    if find(j)!=find(k):
        union(j,k)
        ans += i
    #print(ans)
if ans>final_ans:
    final_ans=ans
ans = 0
tree = [i for i in range(v)]
for i,j,k in (graph):
    if j==0:
        continue
    #print(tree)
    if find(j)!=find(k):
        union(j,k)
        ans += i
    #print(ans)
for i in range(1,N+2):
    if find(1)!=find(i):
        ans = float('inf')
if ans<final_ans:
    final_ans=ans
ans = 0
tree = [i for i in range(v)]
for i,j,k in (graph):
    if j==N+1:
        continue
    #print(tree)
    if find(j)!=find(k):
        union(j,k)
        ans += i
    #print(ans)
for i in range(N+1):
    if find(1)!=find(i):
        ans = float('inf')
if ans<final_ans:
    final_ans=ans
ans = 0
tree = [i for i in range(v)]
for i,j,k in (graph):
    if j==N+1 or j==0:
        continue
    #print(tree)
    if find(j)!=find(k):
        union(j,k)
        ans += i
    #print(ans)
for i in range(1,N+1):
    if find(1)!=find(i):
        ans = float('inf')
if ans<final_ans:
    final_ans=ans
print(final_ans)
