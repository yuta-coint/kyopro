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
primes = sieve_of_eratosthenes(10**6+1)
K = int(input())
temp = 1
ans1 = 0
ans2 = 0
t = K
for i in primes:
    while t%i==0:
        t//=i
ans2 = t
K//=t
for i in range(1,2**(10**6)+1):
    temp*=i
    temp%=K
    if temp==0:
        ans1 = i
        break
print(max(ans1,ans2))

