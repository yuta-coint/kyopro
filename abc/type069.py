N,K = map(int,input().split())
mod= 10**9+7
if N==1:
    print(K)
elif K==1:
    print(0)
elif N==2:
    print(K*(K-1)%mod)
elif K==2:
    print(0)
else:
    print(K*(K-1)%mod*pow(K-2,N-2,mod)%mod)
