def main():
    N,M,B,W = map(int,input().split())
    mod = 998244353
    pas =  [[0 for i in range(51)] for j in range(51)]
    for i in range(51):
        pas[i][0]=1
        pas[0][1]=1
    for i in range(51):
        for j in range(51):
            pas[i][j]=(pas[i][j-1]+pas[i-1][j])%mod
    def BW_cnt(BW):
        BWfac = 1
        for i in range(1,BW+1):
            BWfac *= pow(i,mod-2,mod)
            BWfac %= mod
        temp = [[0 for i in range(M+1)] for j in range(N+1)]
        for i in range(N+1):
            for j in range(M+1):
                if i*j<BW:
                    continue
                S=BWfac
                for k in range(BW):
                    S *= i*j-k
                    S %= mod
                for p in range(i+1):
                    for q in range(j+1):
                        if p == i and q==j:
                            continue
                        S-=(pas[p][i-p]*pas[q][j-q]%mod)*temp[p][q]%mod
                        S%=mod
                temp[i][j] = S
        return(temp)
    black = BW_cnt(B)
    white = BW_cnt(W)
    #print(black)
    #print(white)
    ans = 0
    for i in range(N):
        for j in range(N-i+1):
            for k in range(M):
                for l in range(M-k+1):
                    temp=black[i][k]
                    temp*=white[j][l]
                    temp%=mod
                    temp*=pas[i+j][N-i-j]
                    temp%=mod
                    temp*=pas[i][j]
                    temp%=mod
                    temp*=pas[k+l][M-k-l]
                    temp%=mod
                    temp*=pas[k][l]
                    temp%=mod
                    ans+=temp
                    ans%=mod
    print(ans)
main()