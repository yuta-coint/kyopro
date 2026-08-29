Q=int(input())
import math
import sys,bisect
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
LP = sieve_of_eratosthenes(10**6+1)
small_power = []
power = []
for p in LP:
    temp = p
    while temp<=10**6:
        if temp<=10**3:
            small_power.append(temp)
        power.append(temp)
        temp*= p
s_power = set(power)
prime_2 = []
power.sort()
for p in small_power:
    for q in power:
        if p>=q:
            continue
        if p*q>10**6:
            break
        if p*q in s_power:
            continue
        prime_2.append(p*q)
prime_2.sort()
for _ in range(Q):
    A = int(input())
    A = math.isqrt(A)
    print(prime_2[bisect.bisect_right(prime_2,A)-1]**2)