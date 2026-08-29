#任意の三角形について、最初の2辺は続きにしてはいけない
#つまりその辺が上下関係で真ん中に来てはいけない
##順序関係がついている三角形について、中⇒下⇒上は即死
N = int(input())
pairs = [tuple(map(int,input().split)) for i in range((N*(N-1))>>1)]
d = [[0 for i in range(N)] for j in range(N)]
done = [[0 for i in range(N)] for j in range(N)]
for t in range((N*(N-1))>>1):
    i,j = pairs[t]
    d[i][j]=t
    d[j][i]=t
#ans = [[1 for i in range(N)] for j in range(N)]
ans = []
mod = 10**9+7
for t in range((N*(N-1))>>1):
    chance=2
    i,j = pairs[t]
    for k in range(N):
        if i==j or j==k:
            continue
        if done[i][k]+done[j][k]==1:
            if chance==2:
                chance=1
    done[i][j]=1
    done[j][i]=1
    ans.append(chance)
two = [[[0 for i in range(N)] for j in range(N)] for k in range(N)]
done = [[0 for i in range(N)] for j in range(N)]
for t in reversed(range((N*(N-1))>>1)):
    i,j = pairs[t]
    for l in range(N):
        if done[i]*done[j]==1:

prod = 1
for t in range((N*(N-1))>>1):
    prod*=ans[t]
    prod%=mod
print(prod)