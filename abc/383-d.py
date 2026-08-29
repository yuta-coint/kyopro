import math
import sys
from bisect import bisect_right
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
primes = sieve_of_eratosthenes(2*(10**6))
N = int(input())
ans = 0
for p in primes:
    if p**8<=N:
        ans+=1
#異なる素数を二つかけて2*(10**6)以下にしたい
M = math.floor(math.sqrt(N))
for i in range(len(primes)):
    a = primes[i]
    bu = min(a-1,M//a)
    ans += bisect_right(primes,bu)
print(ans)