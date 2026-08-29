
import math
import sys
input = sys.stdin.readline
def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    #primeは素数判定機
    list_of_prime =[]
    for i in range(n+1):
        if prime[i]:
            list_of_prime.append(i)
    return(list_of_prime)
ans = 1
L,R = map(int,input().split())
#L+1からRまでに素冪が1個増えるごとに1個答えを増やす
#素数であるかを判定し、素冪であるかを判定する。
primes = sieve_of_eratosthenes(10**7+1)
sobeki = set()
for p in primes:
    q = p
    while q<=10**14:
        sobeki.add(q)
        q*=p
LR_primes = [True for i in range(R-L)]
for p in primes:
    fusoku = p-1-(L%p)
    for j in range(fusoku,R-L,p):
        LR_primes[j] = False
for m in range(L+1,R+1):
    if LR_primes[m-(L+1)] or (m in sobeki):
        ans += 1
print(ans)
    