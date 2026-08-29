mod = 998244353
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
#最初の長さ5の処理
N,M = map(int,input().split())
S = [input() for i in range(M)]
S = set(S)
six = min(N,5)
start = []
for ty in range(1<<six):
    temp = ""
    for i in reversed(range(six)):
        if (ty>>i)&1:
            temp+="b"
        else:
            temp+="a"
    flag = 1
    for l in range(six):
        for r in range(l+1,six+1):
            cut = temp[l:r]
            if cut in S:
                flag = 0
    start.append(flag)
if N<=5:
    print(sum(start))
    exit()
illigal = set()
for s in S:
    l = len(s)
    k = 0
    for i in range(l):
        k*=2
        if s[i]=="b":
            k+=1
    while k<64:
        illigal.add(k)
        k+=1<<l
check_matrix = [[0 for j in range(32)] for i in range(32)]
#print(list(illigal))
for i in range(32):
    if not (2*i in illigal):
        check_matrix[2*i%32][i]=1
    if not (2*i+1 in illigal):
        check_matrix[(2*i+1)%32][i]=1
cmp = matrix_pow(check_matrix,N-5,32)
ans = 0
#for i in range(32):
#    print(check_matrix[i])
for i in range(32):
    for j in range(32):
        ans += cmp[i][j]*start[j]
        ans%=mod
print(ans)