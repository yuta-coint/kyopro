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
A = list(map(int,input().split()))
#平方数で割れるだけ割った時に等しい
LP = sieve_of_eratosthenes(500)
for i in range(N):
    if A[i]==0:
        continue
    for p in LP:
        while A[i]%(p*p)==0:
            A[i]//=(p*p)
A.sort()
cnt = 0
pre = -1
ans = 0
zero = 0
for i in range(N):
    if A[i]==0:
        zero+=1
    elif A[i]!=pre:
        ans+=cnt*(cnt-1)//2
        pre = A[i]
        cnt = 1
    else:
        cnt+=1
ans += cnt*(cnt-1)//2
ans += (N*(N-1)-(N-zero)*(N-zero-1))//2
print(ans)
    
