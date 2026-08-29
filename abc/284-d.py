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
primes = sieve_of_eratosthenes(3*(10**6))
from math import sqrt,floor
T = int(input())
for _ in range(T):
    N = int(input())
    for r in primes:
        if N%r==0:
            N//=r
            if N%r==0:
                print(r,N//r)
            else:
                p = floor(sqrt(N)+0.01)
                print(p,r)
            break
                
