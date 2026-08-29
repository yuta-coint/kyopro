import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
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
N =int(input())
X = list(map(lambda x:int(x)-1,input().split()))
C = list(map(int,input().split()))
v=N
e=N
graph = []
tree = [i for i in range(v)]
for i in range(e):
    graph.append([-C[i],i,X[i]])
graph.sort()
ans = 0
for i in range(e):
    #print(tree)
    if find(graph[i][1])!=find(graph[i][2]):
        union(graph[i][1],graph[i][2])
        ans += graph[i][0]
    #print(ans)
print(sum(C)+ans)
