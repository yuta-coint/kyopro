N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
sA = [A[i]^A[i+1] for i in range(N-1)]+[A[0]^A[N-1]]
sB = [B[i]^B[i+1] for i in range(N-1)]+[B[0]^B[N-1]]
hash = [(372,998244353),(609,10**9+7),(83,10**9+9)]
ans = -1
for x,mod in hash:
    poly_A = 0
    poly_B = 0
    temp = set()
    for i in range(N):
        poly_A *= x
        poly_A %= mod
        poly_A += sA[i]
        poly_A %=mod
        poly_B *= x
        poly_B %= mod
        poly_B += sB[i]
        poly_B %= mod
    minus = pow(x,N,mod)
    for i in range(N):
        if poly_A==poly_B:
            temp.add((i,A[i]^B[0]))
        poly_A*=x
        poly_A%=mod
        poly_A+=sA[i]
        poly_A%=mod
        poly_A-=minus*sA[i]%mod
        poly_A%=mod
    if ans == -1:
        ans = temp
    else:
        ans = temp&ans
for t,X in ans:
    print(t,X)
