t = int(input())
mod = 10**9+7
pari = []
for i in range(1,10):
    pari.append(i)
    pari.append(11*i)
for i in range(1,10):
    for j in range(10):
        pari.append(101*i+10*j)
        pari.append(1001*i+110*j)
for i in range(1,10):
    for j in range(10):
        for k in range(10):
            pari.append(i*10001+j*1010+k*100)
pari.sort()
lp = len(pari)
ans = [0 for j in range(4*(10**4)+1)]
for k in reversed(range(lp)):
    for i in range(4*(10**4)+1):
        if pari[k]>i:
            ans[i]=0
            continue
        if pari[k]==i:
            ans[i]=1
            continue
        #if k<lp-1:
        #    ans[i]+=ans[i]
        #ans[i]%=mod
        if i>=pari[k]:
            ans[i]+=ans[i-pari[k]]
        ans[i]%=mod
for _ in range(t):
    n=int(input())
    print(ans[n])
