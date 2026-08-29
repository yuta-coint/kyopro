mod = 998244353
div100 = pow(100,mod-2,mod)
hand24 = pow(100,24,mod)
N,X,Y = map(int,input().split())
d=input()
c = list(d)
#一周回って何も起こらない
cyc = 1
for i in range(24):
    if c[i]=="T":
        cyc*=100-X
        c[i]=X
    else:
        cyc*=100-Y
        c[i]=Y
    cyc%=mod
cyc = pow(cyc,mod-2,mod)
mat = [[0 for i in range(24)] for i in range(24)]
for i in range(24):
    temp = hand24*cyc%mod
    for j in range(24):
        temp*=div100
        temp%=mod
        mat[(i+j+1)%24][i]=temp*c[(i+j+1)%24]%mod
        temp*=100-c[(i+j+1)%24]
        temp%=mod
def cross(m,n):
    t = [[0 for i in range(24)] for j in range(24)]
    for i in range(24):
        for j in range(24):
            for k in range(24):
                t[i][j]+=m[i][k]*n[k][j]%mod
                t[i][j]%=mod
    return(t)
ans = [[0 for i in range(24)] for j in range(24)]
for i in range(24):
    ans[i][i]=1
k = len(bin(N))
for i in reversed(range(k)):
    ans =cross(ans,ans)
    if (N>>i)&1:
        ans = cross(ans,mat)

taka = 0
aoki = 0
for i in range(24):
    if d[i]=="T":
        taka += ans[i][23]
        taka%=mod
    else:
        aoki += ans[i][23]
        aoki %= mod
print(pow(taka+aoki,mod-2,mod)*aoki%mod)