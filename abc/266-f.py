#def main():
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N = int(input())
chk = 0
visited = [False for i in range(N+1)]
mother = [0 for i in range(N+1)]
G = [[] for i in range(N+1)]
edges = []
for i in range(N):
    s,t = map(int,input().split())
    G[s].append(t)
    G[t].append(s)
    edges.append((s,t))
t1,t2 = 0,0
def dfs(v):
    visited[v]=True
    #print(mother)
    for i in G[v]:
        if visited[i]:
            if i!=mother[v]:
                global t1
                global t2
                t1,t2 = i,v
        else:
            mother[i]=v
            dfs(i)
dfs(1)
#print(G)
#print(mother)
#print(t1,t2)
remove = []
remove.append((min(t1,t2),max(t1,t2)))
while True:
    if t1<mother[t1]:
        remove.append((t1,mother[t1]))
    else:
        remove.append((mother[t1],t1))
    #print(t1)
    if mother[t1]!=t2:
        t1 = mother[t1]
    else:
        break
n=N+1
###コピペ
#再帰のおまじないを忘れずに
tree = [i for i in range(n)]
#size = [1 for i in range(n)]
#sys.setrecursionlimit(10**6)
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
remove=set(remove)
for e in edges:
    if e in remove:
        continue
    union(e[0],e[1])
Q = int(input())
for i in range(Q):
    x,y = map(int,input().split())
    if find(x)==find(y):
        print("Yes")
    else:
        print("No")