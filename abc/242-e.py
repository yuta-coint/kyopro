import sys
input = sys.stdin.readline
mod= 998244353
T = int(input())
pow26 = [1]
for i in range(10**6):
    pow26.append((pow26[-1]*26)%mod)
for _ in range(T):
    n = int(input())
    nn = (n+1)//2
    s = input()
    ans = 0
    for i in range(nn):
        k = (ord(s[i])-ord("A"))%26
        ans+=(pow26[nn-i-1]*k)%mod
        ans%=mod
    #AXAを要れるか判定
    for i in range(nn,n):
        if s[i]<s[n-1-i]:
            break
        elif s[i]>s[n-1-i]:
            ans+=1
            break
    else:
        ans+=1
    print(ans%mod)


