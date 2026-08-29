N,M = map(int,input().split())
A = list(map(int,input().split()))
C = list(map(int,input().split()))
B = []
for i in range(M+1):
    t = C[N+M-i]
    for j in range(i):
        if 0<i-j<=N:
            t-=B[j]*A[N-i+j]
    B.append(t//A[N])
B.reverse()
print(*B)