def factorization(numa):
    arr = []
    hp = numa
    for i in range(2, int(-(-numa**0.5//1))+1):
        powa = 0
        while hp%i==0:
            hp //= i
            powa += 1
        if powa>0:
            arr.append([i, powa])
    if hp > 1:
        arr.append([hp,1])
    return(arr)
A,B = map(int,input().split())
if B == 0:
    print(0)
    exit()
fc = factorization(A)
mod = 998244353
ans = 499122177*B%mod
odd = True
non_one = False
if B%2==0:
    odd = True
for p in fc:
    ans *= (1+B*p[1]%mod)
    if B&1 and p[1]&1:
        odd = False
    if p[1]>=2:
        non_one = True
    ans %= mod
if odd and non_one:
    ans -= 499122177
    ans %= mod
print(ans)
