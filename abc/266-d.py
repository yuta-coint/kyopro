def main():
    import sys
    input = sys.stdin.readline
    snukes = [[0 for j in range(5)] for i in range(10**5+1)]
    N = int(input())
    for i in range(N):
        t,x,a = map(int,input().split())
        snukes[t][x]=a
    dp = [-float('inf') for i in range(5)]
    dp[0]=0
    for i in range(1,10**5+1):
        s = snukes[i]
        temp = []
        temp.append(s[0]+max(dp[0],dp[1]))
        for j in range(1,4):
            temp.append(s[j]+max(dp[j-1],dp[j],dp[j+1]))
        temp.append(s[4]+max(dp[4],dp[3]))
        dp = temp
    print(max(dp))
main()