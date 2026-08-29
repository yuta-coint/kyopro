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
N = int(input())
pa = sieve_of_eratosthenes(10**3)
pc = sieve_of_eratosthenes(10**6)
la = len(pa)
lc = len(pc)
ans = 0
from bisect import bisect_right
for i in range(la):
    for k in range(i+1,lc):
        r = min(pc[k]-1,(N//(pa[i]*pa[i]*pc[k]*pc[k])))
        if r<pc[i+1]:
            continue
        #a[i+1]以上r以下の素数を数える
        ans+=bisect_right(pc,r)-(i+1)
print(ans)
        
        
        