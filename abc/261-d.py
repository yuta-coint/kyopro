import sys
input = sys.stdin.readline
def main():
    N,M = map(int,input().split())
    X = list(map(int,input().split()))
    Bonus = [0 for i in range(N+1)]
    for i in range(M):
        c,y = map(int,input().split())
        Bonus[c]=y
    #今のカウンター
    dp = [0 for i in range(N+1)]
    for i in range(N):
        temp = max(dp[1:])
        for j in reversed(range(1,i+2)):
            dp[j]=dp[j-1]+Bonus[j]+X[i]
        dp[0]=temp
    print(max(dp))
main()