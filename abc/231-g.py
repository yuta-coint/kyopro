mod = 998244353
N,K = map(int,input().split())
A = list(map(int,input().split()))
sym = [[0 for j in range(N)] for i in range(N)]
sym[0][0]=A[0]
for j in range(1,N):
    sym[0][j]=A[j]+sym[0][j-1]
for i in range(1,N):
    for j in range(i,N):
        sym[i][j] = (sym[i-1][j-1]*A[j]%mod+sym[i][j-1])%mod
npow = [1]
n_rev = pow(N,mod-2,mod)
for i in range(N):
    npow.append(npow[-1]*n_rev%mod)
Ki = [1]
for i in range(N+1):
    Ki.append(Ki[-1]*(K-i)%mod)
#print(sym)
#print(Ki)
#print(n_rev)
ans = Ki[N]*npow[N]%mod
for t in range(N):
    ans+=sym[N-t-1][N-1]*npow[t]%mod*Ki[t]%mod
    #print(t,sym[N-t-1][N-1])
    ans%=mod
print(ans)
