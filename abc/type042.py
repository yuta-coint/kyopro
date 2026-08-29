k = int(input())
ans = [1,1,2,4,8,16,32,64,128,256]
mod = 10**9+7
if k>=11:
    for i in range(10,k+1):
        a = 0
        for j in range(1,10):
            a += ans[i-j]
        ans.append(a%mod)
if k%9==0:
    print(ans[k])
else:
    print(0)
