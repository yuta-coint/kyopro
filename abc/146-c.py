mod = 998244353
N = int(input())
dp = [0 for i in range(N+1)]
all_case = pow(2,pow(2,N,mod-1),mod)
bll_case = pow(2,(pow(2,N,mod-1)-(N**2)%(mod-1))%(mod-1),mod)
print((all_case-bll_case)%mod)

N = int(input())
ans=0
#各集合が条件を満たすか確認
for i in range(2**(2**N)):
    #jは空でない部分集合
    for j in range(2**(2**N)):
        if i&j != j:
            continue
        if j == 0:
            continue
        xo = 0
        cnt=0
        for k in range(2**N):
            if (j>>k)&1:
                cnt+=1
                xo^=k
        if xo == 0 and cnt%2==0:
            ans+=1
            break
print(ans)

