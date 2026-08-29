N,X = map(int,input().split())
T = list(map(int,input().split()))
remaining_time = [0 for i in range(2*(10**4)+5)]
mod = 998244353
prob = pow(N,mod-2,mod)
remaining_time[0]=1
ans = 0
for i in range(X+1):
    #曲の入れ替え
    for music in range(N):
        remaining_time[i+T[music]]+=prob*remaining_time[i]%mod
        remaining_time[i+T[music]]%=mod
    if i>=X-T[0]+1:
        ans+=prob*remaining_time[i]%mod
        ans%=mod
print(ans)