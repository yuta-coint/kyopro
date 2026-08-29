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
primes = sieve_of_eratosthenes(1100)
#最大公約数として取りうる値のうち、Aで割り切れるもので最大？
#p^{k}の倍数がK個ありますか？をそれぞれについて調べることになる？
div_point = [0 for i in range(10**6+1)]
N,K = map(int,input().split())
A=list(map(int,input().split()))
ok = set()
for i in range(N):
    for d in range(1,10**3+1):
        if d*d>A[i]:
            break
        if A[i]%d==0:
            if d*d!=A[i]:
                div_point[A[i]//d]+=1
            div_point[d]+=1
for i in range(N):
    ans = 0
    for d in range(1,10**3+1):
        if d*d>A[i]:
            break
        if A[i]%d==0:
            if div_point[d]>=K:
                if d>ans:
                    ans = d
            if div_point[A[i]//d]>=K:
                ans = d
                break
    print(ans)

    