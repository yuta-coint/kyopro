from itertools import permutations
N,M = map(int,input().split())
mat = [[-10**24 for i in range(N)] for j in range(N)]
for i in range(M):
    A,B,C = map(int,input().split())
    mat[A-1][B-1]=C
    mat[B-1][A-1]=C
ans = 0
for p in permutations(range(N),N):
    temp = 0
    for i in range(N-1):
        temp += mat[p[i]][p[i+1]]
        if temp>ans:
            ans=temp
print(ans)
