N=  int(input())
A = list(map(int,input().split()))
A.reverse()
small = []
mod = 998244353
ans = []
for i in range(N):
    #i個目が黒い
    if A[i]<500:
        if i-A[i]>=0:
            ans.append((small[i-A[i]][A[i]]+1)%mod)
        else:
            ans.append(1)
    else:
        temp = i-A[i]
        cnt = 1
        while temp>=0:
            cnt+=ans[temp]
            cnt %= mod
            temp-=A[i]
        ans.append(cnt)
    sl =[0]
    for width in range(1,500):
        if i-width>=0:
            sl.append((small[i-width][width]+ans[i])%mod)
        else:
            sl.append(ans[-1])
    small.append(sl)
print(ans[-1])