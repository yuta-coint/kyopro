n = int(input())
al = [0 for i in range(n+1)]
a = [0 for i in range(n+1)]
#gaにagは含まれない
mod = 10**9+7
mat = [1 for i in range(256)]
ans = [1 for i in range(64)]
out = [108,109,110,111,120,121,122,123,156,157,158,159,99,103,107,75,91,107,27,91,155,219,30,94,158,222,39,103,167,231]
for i in out:
    mat[i]=0
ans[27]=0
ans[30]=0
ans[39]=0
for _ in range(n-3):
    temp = [0 for __ in range(64)]
    #iは前三つの並び
    for i in range(64):
        #付け足す文字
        for j in range(4):
            temp[(4*i+j)%64]+=ans[i]*mat[4*i+j]
            temp[(4*i+j)%64]%=mod
    ans = temp
print(sum(ans)%mod)
