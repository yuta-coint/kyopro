def main():
    import sys
    input = sys.stdin.readline
    N = int(input())
    cost = [[0]+list(map(int,input().split())) for i in range(2**N)]
    dp = [0 for i in range(2**(N-1))]+[max(cost[2*i][1],cost[2*i+1][1]) for i in range(2**(N-1))]+[0 for i in range(2**N)]
    fls =[N+1]
    for i in range(N+1):
        fls += [N-i for j in range(1<<i)]
    #print(len(fls))
    for i in reversed(range(1,2**(N-1))):
        fl = fls[i]
        #print(fl,i,dp)
        for j in range(i<<fl,(i+1)<<fl):
            t = cost[j-(1<<N)][fl]
            for k in range(fl):
                t+=dp[(j>>k)^1]
            dp[i] = max(dp[i],t)
    print(dp[1])
main()


