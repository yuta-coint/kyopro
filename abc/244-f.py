import sys
input = sys.stdin.readline
N,M = map(int,input().split())
G1 = [[0 for i in range(N)] for j in range(N)]
G  =[[] for i in range(N)]
for i in range(M):
    u,v = map(lambda x:int(x)-1,input().split())
    G1[u][v]=1
    G1[v][u]=1
    G[u].append(v)
    G[v].append(u)
ans = [[-1 for i in range(2**N)] for j in range(N)]
import queue
q = queue.Queue()
ans[0][0] = 0
for i in range(N):
    ans[i][1<<i]=1
    q.put((i,1<<i))
while not q.empty():
    v = q.get()
    s,c = v[0],v[1]
    for t in G[s]:
        if ans[t][c^(1<<t)]>=0:
            continue
        ans[t][c^(1<<t)]=ans[s][c]+1
        q.put((t,c^(1<<t)))
a = 0
for i in range(2**N):
    temp = float('inf')
    for j in range(N):
        if ans[j][i]>=0 and ans[j][i]<temp:
            temp = ans[j][i]
    a+=temp
print(a)