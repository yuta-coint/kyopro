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
    return(prime)
p = sieve_of_eratosthenes(300)
a,b,c,d = map(int,input().split())
for i in range(a,b+1):
    for j in range(i+c,i+d+1):
        if p[j]:
            break
    else:
        print("Takahashi")
        break
else:
    print("Aoki")

