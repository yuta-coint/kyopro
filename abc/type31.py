import math
n,K = map(int,input().split())
def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = math.ceil(math.sqrt(n))
    for i in range(2, sqrt_n):
        if prime[i]:
            for j in range(2*i, n+1, i):
                prime[j] = False
    lip = []
    for i in range(n):
        if prime[i]:
            lip.append(i)            
    return lip
p = sieve_of_eratosthenes(n)
factor = [0 for i in range(n+1)]
for q in p:
    for i in range(n//q):
        factor[(i+1)*q]+=1
ans = 0
for i in range(n+1):
    if factor[i]>=K:
        ans+=1
print(ans)