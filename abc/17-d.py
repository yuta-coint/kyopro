import sys
input = sys.stdin.readline
n,m = map(int,input().split())
check = [-1 for i in range(m+1)]
ty = []
cnt = -1
for i in range(n):
    f = int(input())
    if check[f]<=cnt:
        check[f]=i
    else:
        cnt = check[f]
        check[f]=i
    ty.append(cnt)
dp = [1]
cumdp = [1]
mod = 10**9+7
for i in range(n):
    if ty[i]>=0:
        temp = cumdp[i]-cumdp[ty[i]]
    else:
        temp = cumdp[i]
    dp.append(temp%mod)
    cumdp.append((temp+cumdp[-1])%mod)
print(dp[-1])
