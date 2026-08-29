N,p = map(int,input().split())
def mat_times(P,Q,N):
    R = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                R[i][j]+=P[i][k]*Q[k][j]
            #次の一行はmod pで扱うための物である。
            R[i][j]%=p
    return R
def mat_pow(M,m1,N):
    m = m1
    R = [[0 for i in range(N)] for j in range(N)]
    for i in range(N):
        R[i][i]=1
    bi = []
    while m>0:
        bi.append(m&1)
        m//=2
    bi.reverse()
    for b in bi:
        R = mat_times(R,R,N)
        if b==1:
            R = mat_times(R,M,N)
    return R
A = [list(map(int,input().split())) for i in range(N)]
K = 0
for i in range(N):
    for j in range(N):
        if A[i][j] == 0:
            K+=1
if K&1:
    pari = -1
else:
    pari = 1
if p==2:
    ans = [[N%2 for j in range(N)] for i in range(N)]
elif p==3:
    ans = mat_pow(A,p,N)
    for i in range(N):
        for j in range(N):
            ans[i][j]*=pari
            ans[i][j]%=p
    #print(ans)
    for i in range(N):
        for j in range(N):
            if i!=j:
                if A[i][i]==0:
                    ans[i][j]+=A[i][j]*pari
                if A[j][j]==0:
                    ans[i][j]+=A[i][j]*pari
                if A[i][j]==0:
                    ans[i][j]+=A[j][i]*pari
                ans[i][j]%=p
else:
    ans = mat_pow(A,p,N)
    for i in range(N):
        for j in range(N):
            ans[i][j]*=pari
            ans[i][j]%=p
    #print(ans)
    for i in range(N):
        for j in range(N):
            if i!=j:
                if A[i][i]==0:
                    ans[i][j]+=A[i][j]*pari
                if A[j][j]==0:
                    ans[i][j]+=A[i][j]*pari
                ans[i][j]%=p
for i in range(N):
    print(*ans[i])