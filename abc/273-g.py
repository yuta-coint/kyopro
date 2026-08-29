N=int(input())
mod = 998244353
fac = [1]
for i in range(1,N+1):
    fac.append(fac[-1]*i%mod)
inv_fac = [pow(fac[-1],mod-2,mod)]
for i in reversed(range(1,N+1)):
    inv_fac.append(inv_fac[-1]*i%mod)
inv_fac.reverse()
half = pow(2,mod-2,mod)
R = list(map(int,input().split()))
C = list(map(int,input().split()))
if sum(R)!=sum(C):
    print(0)
    exit()
R2,R1 = R.count(2),R.count(1)
C2,C1 = C.count(2),C.count(1)
#横列…2がi個,1がR1個　縦列…2がj個、1が(i-j)*2+R1個の時の場合の数
all_two_ans = [[0 for i in range(C2+1)] for j in range(R2+1)]
for j in range(C2+1):
    if R1-2*j<0:
        break
    all_two_ans[0][j]=fac[R1]*pow(half,j,mod)%mod
for i in range(1,R2+1):
    for j in range(C2+1):
        if (i-j)*2+R1<0:
            break
        all_two_ans[i][j]=all_two_ans[i-1][j]*((2*i-2*j+R1-1)*(2*i-2*j+R1)//2)%mod
        if j>=1:
            all_two_ans[i][j]+=all_two_ans[i-1][j-1]*(2*i-2*j+R1)%mod*j%mod
            all_two_ans[i][j]%=mod
        if j>=2:
            all_two_ans[i][j]+=all_two_ans[i-1][j-2]*(j*(j-1)//2)%mod
            all_two_ans[i][j]%=mod
#print(all_two_ans)
ans = 0
for i in range(min(R2,C2)+1):
    ans+=inv_fac[R2-i]*inv_fac[C2-i]%mod*fac[R2]%mod*fac[C2]%mod*all_two_ans[R2-i][C2-i]%mod*inv_fac[i]%mod
    ans%=mod
print(ans)