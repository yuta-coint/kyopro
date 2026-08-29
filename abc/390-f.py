from bisect import bisect
N = int(input())
A = list(map(int,input().split()))
#-1が入らない区間-Nが入らない区間+iが入るがi\pm 1が入らない区間
#iが入る区間の数をかぞえる。
include = [0 for i in range(N)]
last = [-1 for i in range(N)]
toujo = [[] for i in range(N)]
for i in range(N):
    include[A[i]-1] += (N-i)*(i-last[A[i]-1])
    last[A[i]-1] = i
    toujo[A[i]-1].append(i)
all_interval = N*(N+1)//2
for i in range(N):
    toujo[i].append(N)
#iとi+1が両方入る区間
pair = [0 for i in range(N-1)]
last = [-1 for i in range(N)]
for i in range(N):
    if A[i]!=1:
        pair[A[i]-2] += (N-toujo[A[i]-2][bisect(toujo[A[i]-2],i)])*(i-max(last[A[i]-1],last[A[i]-2]))
    if A[i]!=N:
        pair[A[i]-1] += (N-toujo[A[i]][bisect(toujo[A[i]],i)])*(i-max(last[A[i]-1],last[A[i]]))
    last[A[i]-1] = i
#print(include,pair)
print(sum(include)-sum(pair))