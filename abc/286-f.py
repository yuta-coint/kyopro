import sys
print(108)
sys.stdout.flush()
primes = [4,9,5,7,11,13,17,19,23]
prime_sum = [0]
prime_mul = [1]
A = []
cnt=1
for p in primes:
    prime_sum.append(prime_sum[-1]+p)
    prime_mul.append(prime_mul[-1]*p)
    for _ in range(p-1):
        cnt+=1
        A.append(cnt)
    cnt+=1
    A.append(cnt-p)
print(*A)
sys.stdout.flush()
B = list(map(int,input().split()))
N = B[0]-1
for i in range(1,9):
    amari = B[prime_sum[i]]-1-prime_sum[i]
    for k in range(primes[i]):
        if N%primes[i]==amari:
            break
        N+=prime_mul[i]
print(N)
sys.stdout.flush()
