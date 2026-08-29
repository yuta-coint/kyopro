import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
v,e,q = map(int,input().split())
graph = []
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

for i in range(e):
    s,t,w = map(int,input().split())
    s-=1
    t-=1
    graph.append([w,s,t])
graph.sort()
span = [[] for i in range(v)]
que = [list(map(int,input().split()))+[i] for i in range(q)]
que.sort(key=lambda x: x[2])
cnt = 0
ans = ["No" for i in range(q)]
for i in range(e):
    while cnt<q:
        if que[cnt][2]<graph[i][0]:
            if find(que[cnt][0]-1)!=find(que[cnt][1]-1):
                ans[que[cnt][3]]="Yes"
            cnt+=1
        else:
            break
    #print(tree)
    if find(graph[i][1])!=find(graph[i][2]):
        union(graph[i][1],graph[i][2])
    #print(ans)
    
while cnt<q:
    if find(que[cnt][0]-1)!=find(que[cnt][1]-1):
        ans[que[cnt][3]]="Yes"
    cnt+=1
for i in range(q):
    print(ans[i])
