N=int(input())
A = list(map(int,input().split()))
max_A=[0 for i in range(N)]
ma = -1
for i in range(N):
    if A[i] > ma:
        ma = A[i]
    max_A[i] = ma
S = 0
SS = 0
for i in range(N):
    S += A[i]
    SS += S
    print(SS + max_A[i] * (i + 1))