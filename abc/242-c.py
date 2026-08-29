ans = [1 for i in range(9)]
n = int(input())
mod= 998244353
for _ in range(1,n):
    temp = [0 for _ in range(9)]
    temp[0]=ans[0]+ans[1]
    temp[8]=ans[7]+ans[8]
    for i in range(1,8):
        temp[i]=ans[i-1]+ans[i]+ans[i+1]
    for i in range(9):
        ans[i]=temp[i]%mod
print(sum(ans)%mod)
