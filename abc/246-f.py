##mの(pow乗)
def bigpower(base,pow):
    num = 1
    for i in reversed(range(len(bin(pow)))):
        num = num*num%mod
        if pow>>i & 1:
            num = num*base%mod
        i+=1
    return(num)
import sys
input = sys.stdin.readline
mod = 998244353
n,l = map(int,input().split())
abcpow = [bigpower(i,l) for i in range(27)]
S = [set(list(input())) for i in range(n)]
abc = set(list("abcdefghijklmnopqrstuvwxyz"))
t = []
ans = 0
for i in range(1,2**n):
    k = abc
    cnt = 1
    for j in range(n):
        if i>>j & 1:
            k = k & S[j]
            cnt+=1
    ans+=abcpow[len(k)]*((-1)**cnt)
    ans%=mod
print(ans)



