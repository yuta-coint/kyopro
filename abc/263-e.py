def main():
    N = int(input())
    A = list(map(int,input().split()))
    P = [0 for i in range(N)]
    sP = [0 for i in range(N+1)]
    mod = 998244353
    for i in reversed(range(N-1)):
        P[i] = (sP[i+1]-sP[i+A[i]+1]+A[i]+1)%mod
        P[i] *= pow(A[i],mod-2,mod)
        P[i]%=mod
        sP[i] = (sP[i+1]+P[i])%mod
    #print(P)
    print(P[0])
main()