mod = 10**9+7
#m行n列×n行l列
def matrix_mul(A,B,m,n,l):
    r = [[0 for j in range(l)] for i in range(m)]
    for i in range(m):
        for j in range(l):
            for k in range(n):
                r[i][j]+=A[i][k]*B[k][j]%mod
                r[i][j]%=mod
    return r

def matrix_pow(mat,k,n):
    dig = len(bin(k))
    r = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        r[i][i]=1
    for i in reversed(range(dig)):
        r = matrix_mul(r,r,n,n,n)
        if (k>>i)&1:
            r = matrix_mul(r,mat,n,n,n)
    return r

N,K = map(int,input().split())
a = [list(map(int,input().split())) for i in range(N)]
check = matrix_pow(a,K,N)
ans = 0
for i in range(N):
    ans+=sum(check[i])%mod
    ans%=mod
print(ans)