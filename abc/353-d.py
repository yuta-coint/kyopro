N = int(input())
A = list(map(int,input().split()))
keta = []
for i in range(N):
    for d in range(11):
        if A[i]<10**d:
            keta.append(d)
            break
mod = 998244353
#下の位として使う回数がi回ある。上の位としての使われ方は累積和で持つ。
ruiseki = 0
ans = 0
for i in range(N):
    ans+=A[i]*i%mod
    ans%=mod
    ans+=ruiseki*(10**keta[i])%mod
    ans%=mod
    ruiseki+=A[i]
    ruiseki%=mod
print(ans)