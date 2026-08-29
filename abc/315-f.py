#70個以上通るものは全部無視すればいい
import sys
input = sys.stdin.readline
N=int(input())
check_points = [tuple(map(int,input().split())) for i in range(N)]
dp = [[10**24 for cnt in range(57)] for i in range(N)]
dp[0][0]=0
from math import sqrt
def dist(s,t):
    return(sqrt((check_points[s][0]-check_points[t][0])**2+(check_points[s][1]-check_points[t][1])**2))
for i in range(1,N):
    #j個前からj-1個スキップすると
    dst = [dist(i,i-j) for j in range(min(i+1,60))]
    for skipped in range(57):
        for j in range(1,i+1):
            if skipped-j+1<0 or i-j<0:
                break
            if dp[i][skipped]>dp[i-j][skipped-j+1]+dst[j]:
                dp[i][skipped]=dp[i-j][skipped-j+1]+dst[j]
ans = dp[N-1][0]
for skipped in range(1,57):
    if ans>dp[N-1][skipped]+(1<<(skipped-1)):
        ans = dp[N-1][skipped]+(1<<(skipped-1))
print(ans)