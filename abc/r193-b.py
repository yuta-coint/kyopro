mod = 998244353
N = int(input())
S = list(input())
#両端なし、両端足して1以下、両端足して1以上、両端足して1、左端に自由枠、両端に自由枠、右端に自由枠
a = [0]
b = [0]
c = [0]
d = [0]
e = [0]
f = [0]
g = [0]
if S[1] == "0":
    a.append(1)
    b.append(2)
    c.append(2)
    d.append(1)
    e.append(2)
    f.append(3)
    g.append(2)
else:
    a.append(2)
    b.append(3)
    c.append(3)
    d.append(2)
    e.append(3)
    f.append(4)
    g.append(3)
for i in range(1,N-1):
    if S[i+1]=="0":
        a.append(2*a[i]%mod)
        b.append((a[i]+b[i]+e[i])%mod)
        c.append((a[i]+c[i]+e[i])%mod)
        d.append((2*a[i]+d[i])%mod)
        e.append((2*e[i])%mod)
        f.append((2*e[i]+f[i])%mod)
        g.append((2*a[i]+g[i])%mod)
    else:
        a.append((2*a[i]+g[i])%mod)
        b.append((a[i]+b[i]+e[i]+f[i])%mod)
        c.append((a[i]+c[i]+e[i]+f[i])%mod)
        d.append((2*a[i]+b[i]+c[i])%mod)
        e.append((2*e[i]+f[i])%mod)
        f.append((2*e[i]+2*f[i])%mod)
        g.append((2*a[i]+2*g[i])%mod)
if S[0]=="1":
    print((2*a[-1]+b[-1]+c[-1])%mod)
else:
    print((2*a[-1]+d[-1])%mod)