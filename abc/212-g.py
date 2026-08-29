P=int(input())
def factorization(numa):
    arr = []
    hp = numa
    for i in range(2, int(-(-numa**0.5//1))+1):
        powa = 0
        while hp%i==0:
            hp //= i
            arr.append(i)
    if hp>1:
        arr.append(hp)
    return(arr)
def phi(numb):
    phin = numb
    for i in p:
        if numb%i!=0:
            continue
        phin *= i-1
        phin //= i
    return(phin)
#約数列挙
dev = []
for i in range(1,10**6+1):
    if i*i==P-1:
        dev.append(i)
    elif i*i>P-1:
        break
    else:
        if (P-1)%i==0:
            dev.append(i)
            dev.append((P-1)//i)
p = set(factorization(P-1))
ans = 0
mod = 998244353
for i in dev:
    ans+=i*phi(i)%mod
    ans%=mod
print((ans+1)%mod)