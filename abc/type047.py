N = int(input())
S = list(input())
T = list(input())
mod = 998244353
h = 372
power = [1]
for i in range(10**6+1):
    power.append(power[-1]*h%mod)
for i in range(N):
    if S[i]=="R":
        S[i]=0
    elif S[i]=="G":
        S[i]=1
    else:
        S[i]=2
    if T[i]=="R":
        T[i]=0
    elif T[i]=="G":
        T[i]=1
    else:
        T[i]=2
ans = 0
for c in range(3):
    s_hash = 0
    t_hash = 0
    for i in range(N):
        s_hash*=h
        s_hash%=mod
        s_hash+=S[i]
        t_hash+=power[i]*((c-T[N-1-i])%3)%mod
        t_hash%=mod
        if s_hash==t_hash:
            ans+=1
    s_hash = 0
    t_hash = 0
    for i in range(N-1):
        s_hash*=h
        s_hash%=mod
        s_hash+=(c-T[i])%3
        t_hash+=power[i]*(S[N-1-i]%3)%mod
        t_hash%=mod
        if s_hash==t_hash:
            ans+=1
print(ans)
