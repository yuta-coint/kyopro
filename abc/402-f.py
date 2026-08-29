N,M = map(int,input().split())
#半分全列挙
A= [list(map(int,input().split())) for i in range(N)]
for i in range(N):
    for j in range(N):
        A[i][j] = pow(10,2*N-2-i-j,M)*A[i][j]%M
mae = [[] for i in range(N)]
for bits in range(1<<(N-1)):
    i,j = 0,0
    score = A[0][0]
    for k in range(N-1):
        if (bits>>k)&1:
            i+=1
        else:
            j+=1
        score += A[i][j]
        score %= M
    mae[i].append(score)
usiro = [[] for i in range(N)]
for bits in range(1<<N):
    i,j = N-1,N-1
    score = 0
    for k in range(N-1):
        score += A[i][j]
        score %= M
        if (bits>>k)&1:
            i-=1
        else:
            j-=1
    usiro[i].append(score)
#Mを上回らないやつとMを上回るやつで比べる。
for i in range(N):
    mae[i].sort()
from bisect import bisect_right
ans = 0
for i in range(N):
    Len_mae =len(mae[i])
    for J in usiro[i]:
        if (J+mae[i][-1])%M>ans:
            ans = (J+mae[i][-1])%M
        b = bisect_right(mae[i],M-1-J)
        if b>0:
            chk = mae[i][b-1]
            if chk + J>ans:
                ans= chk+J
print(ans)