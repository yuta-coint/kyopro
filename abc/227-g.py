mod = 998244353
# limit 以下の全ての素数を返す
def list_primes(limit):
    primes = []
    is_prime = [True] * (limit + 1)
    is_prime[0] = False
    is_prime[1] = False

    for p in range (0, limit + 1):
        if not is_prime[p]:
            continue
        primes.append(p)
        for i in range(p*p, limit + 1, p):
            is_prime[i] = False

    return primes
def cn(p,m):
    x = 0
    while m>=p:
        x+=m//p
        m//=p
    return(x)
pr = list_primes(10**6)
n,k = map(int,input().split())
a = [n-k+1+i for i in range(k)]
ans1 = []
for i in pr:
    ans1.append(cn(i,n)-cn(i,k)-cn(i,n-k))
    start = ((n-k)//i+1)*i-(n-k+1)
    for j in range(start,k,i):
        while a[j]%i==0:
            a[j]//=i
ans = 1
for i in ans1:
    ans*=i+1
    ans%=mod
for i in a:
    if i!=1:
        ans*=2
        ans%=mod
print(ans)

        

