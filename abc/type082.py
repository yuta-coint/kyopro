mod = 10**9+7
L,R = map(int,input().split())
ans = 0
half  = pow(2,mod-2,mod)
def sumpow1(X):
    return(X%mod*(X+1)%mod*half%mod)
for keta in range(1,20):
    ##10**(i-1)以上10**(i)未満
    if L>=10**keta or R<10**(keta-1):
        continue
    ans+=(sumpow1(min(10**keta-1,R))-sumpow1(max(10**(keta-1)-1,L-1)))%mod*keta%mod
    ans%=mod
print(ans)
