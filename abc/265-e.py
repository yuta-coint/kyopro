def main():
    import sys
    input = sys.stdin.readline
    N,M = map(int,input().split())
    A,B,C,D,E,F = map(int,input().split())
    mod = 998244353
    BAN = []
    big = 2*(10**9)+5
    for i in range(M):
        x,y = map(int,input().split())
        BAN.append(big*x+y)
    BAN  =set(BAN)
    d = {}
    cnt=0
    for i in range(N+1):
        for j in range(N-i+1):
            for k in range(N-i-j+1):
                d[i*301*301+j*301+k] = cnt
                cnt+=1
    check = [True for i in range(cnt+1)]
    dp = [0 for i in range(cnt+1)]
    for i in range(N+1):
        for j in range(N-i+1):
            for k in range(N-i-j+1):
                if big*(A*i+C*j+E*k)+B*i+D*j+F*k in BAN:
                    check[d[i*301*301+j*301+k]]=False
    for i in range(N+1):
        for j in range(N-i+1):
            for k in range(N-i-j+1):
                if check[d[i*301*301+j*301+k]]==False:
                    continue
                temp = 0
                if i!=0:
                    temp=dp[d[(i-1)*301*301+j*301+k]]
                if j!=0:
                    temp+=dp[d[i*301*301+(j-1)*301+k]]
                    temp%=mod
                if k!=0:
                    temp+=dp[d[i*301*301+j*301+k-1]]
                    temp%=mod
                dp[d[i*301*301+j*301+k]]=temp
                if i==0 and j==0 and k==0:
                    dp[0]=1
    ans = 0
    for i in range(N+1):
        for j in range(N-i+1):
            ans+=dp[d[i*301*301+j*301+N-i-j]]
            ans%=mod
    print(ans)
main()
