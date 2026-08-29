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
        a = []
        for i in range(2,n+1):
            if prime[i]:
                a.append(i)
        return(a)
    prm = sieve_of_eratosthenes(10**6)
    N = int(input())
    L=len(prm)
    cnt=0
    ans = 0
    for i in reversed(range(L)):
        p = N//(prm[i]**3)
        if p>=prm[i]:
            cnt=i
        else:
            while prm[cnt]<=p:
                cnt+=1
        ans+=cnt
    print(ans)
main()

