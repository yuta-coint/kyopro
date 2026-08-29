n = int(input())
a = list(map(int,input().split()))
d = {a[0]:0}
d2 = {}
mod = 998244353
ans = 1
s = a[0]
ansSum = [1,2]
if n==1:
    print(1)
else:
    for i in range(1,n-1):
        s+=a[i]
        if s in d:
            ans = ansSum[i]-ansSum[d[s]]
            d[s]=i
        else:
            ans = ansSum[i]
            d[s]=i
        ansSum.append((ansSum[-1]+ans)%mod)
    print(ansSum[-1])
