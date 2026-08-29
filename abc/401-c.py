N,K = map(int,input().split())
A = [1 for i in range(K)]
sum_A = [i for i in range(K+1)]
mod = 10**9
if N<K:
    print(1)
    exit()
for i in range(K,N+1):
    A.append((sum_A[i]-sum_A[i-K])%mod)
    sum_A.append((sum_A[-1]+A[-1])%mod)
print(A[N])
