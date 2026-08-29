def main():
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
    p = sieve_of_eratosthenes(50000)
    from random import randint
    N=int(input())
    A = list(map(int,input().split()))
    ans = -1
    for q in p:
        if q==2:
            q=4
        d = {}
        for i in range(N):
            s = A[i]%q
            if s in d:
                d[s]+=1
                if d[s]==N//2+1:
                    ans=q
                    break
            else:
                d[s]=1
    #クソデカ素数で割り切れるか判定
    for _ in range(80):
        while True:
            t = randint(0,N*N-1)
            a = t%N
            b = t//N
            if a!=b:
                break
        sa = abs(A[b]-A[a])
        if sa<50000:
            continue
        for q in p:
            while sa%q==0:
                sa//=q
                if sa<50000:
                    break
        if sa>=50000:
            t=A[a]%sa
            cnt=0
            for i in range(N):
                if A[i]%sa==t:
                    cnt+=1
            if cnt>N//2:
                ans=sa
        if ans>0:
            break
    print(ans)
main()