import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
import pypyjit
pypyjit.set_param('max_unroll_recursion=-1')
import copy
N,E =  map(int,input().split())
G=[[] for i in range(N)]
A = list(map(lambda x:int(x)-1,input().split()))
B = list(map(lambda x:int(x)-1,input().split()))
G_pair = []
for i in range(E):
    a,b=A[i],B[i]
    G[a].append(b)
    G[b].append(a)
    G_pair.append([a,b])
for i in range(N):G[i].sort()
ord = [None for i in range(N)]
check=[0 for i in range(N)]
mother = [None for i in range(N)]
lowlink = [None for i in range(N)]
counter = 0
ser = []
def dfs(v):
    global counter
    ord[v]=counter
    lowlink[v]=ord[v]
    counter+=1
    check[v]=1
    for i in G[v]:
        if check[i]==0:
            mother[i] = v
            dfs(i)
            lowlink[v] = min(lowlink[v],lowlink[i])
        elif i != mother[v]:
            lowlink[v] = min(lowlink[v],ord[i])
dfs(0)
#print(ord)
#print(lowlink)
#print(mother)
for i in range(E):G_pair[i].sort()
#橋番号の一覧
non_briges = set()
for i in range(E):
    b = G_pair[i]
    if ord[b[0]]<lowlink[b[1]] or ord[b[1]]<lowlink[b[0]]:
        continue
    non_briges.add(i)
G = [[] for i in range(N)]
for i in non_briges:
    G[A[i]].append((B[i],i))
    G[B[i]].append((A[i],i))
for i in range(E):G_pair[i].sort()
for i in reversed(range(N)):
    if G[i]==[]:
        continue
    while 
    t,s = 
