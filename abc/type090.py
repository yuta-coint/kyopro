import sys
sys.setrecursionlimit(10**7)
N,K = map(int,input().split())
mod = 998244353
#小課題1,2
if K==1:
    N+=1
    #1が連続しなければいい
    a,b,c,d = 1,0,0,1
    for i in reversed(range(45)):
        a,b,c,d = (a*a%mod+b*c%mod)%mod,(a*b%mod+b*d%mod)%mod,(a*c%mod+c*d%mod)%mod,(c*b%mod+d*d%mod)%mod
        if (N>>i)&1:
            a,b,c,d = (a+b)%mod,a,(c+d)%mod,c
    print(a)
    exit()
#小課題3
if N<=6 and K<=6:
    ans = 0
    def solve(i,seq):
        global ans
        if i==N:
            flag = 0
            for l in range(N):
                for r in range(l+1,N+1):
                    if min(seq[l:r])*(r-l)>K:
                        flag=1
                        break
                if flag==1:
                    break
            if flag==0:
                ans+=1
        else:
            for j in range(K+1):
                solve(i+1,seq+[j])
    solve(0,[])
    print(ans)
    exit()
if N<=10000 and K<=10000:
    dp = [[]]
    dp.append([i+1 for i in reversed(range(K+1))])
    for m in range(2,N+1):
        temp = []
        pat = 0
        for k in reversed(range(K//m+1)):
            pat += (dp[m-1][k+1]+dp[m-1][k])%mod
            pat %= mod
            for t in range(1,m-1):
                pat+=dp[t][k]*dp[m-1-t][k+1]%mod
                pat%=mod
            temp.append(pat)
        temp.reverse()
        temp.append(0)
        dp.append(temp)
    print(dp[N][0])
    exit()
#畳み込みを頑張る
def convolution(X,Y):
    return(X)
if N<=10**5:
    dp = [[]]
    dp.append([i+1 for i in reversed(range(K+1))])
    for m in range(2,N+1):
        temp = []
        pat = 0
        for k in reversed(range(K//m+1)):
            pat += (dp[m-1][k+1]+dp[m-1][k])%mod
            pat %= mod
            for t in range(1,m-1):
                pat+=dp[t][k]*dp[m-1-t][k+1]%mod
                pat%=mod
            temp.append(pat)
        temp.reverse()
        temp.append(0)
        dp.append(temp)
    print(dp[N][0])
    exit()