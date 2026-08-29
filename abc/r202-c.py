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
def divisors(m):
    div = set()
    for i in range(1, int(-(-m**0.5//1))+1):
        if m%i==0:
            div.add(i)
            if i!= m//i:
                div.add(m//i)
    return(sorted(list(div)))
mod = 998244353
N = int(input())
A = list(map(int, input().split()))
nine = pow(9, -1, mod)
#各数の倍数が何個あるかを管理する。
divs = set()
prime_list = sieve_of_eratosthenes(10**6)
repyu = [1]
for i in range(1, 10**6):
    repyu.append(repyu[-1] * 10 % mod)
for i in range(1,10**6):
    repyu[i] -= 1
    repyu[i] %= mod
    repyu[i] *= nine
    repyu[i] %= mod
ans = 1
from itertools import combinations
for i in range(N):
    ans *= repyu[A[i]]
    ans %= mod
    divisors_a = divisors(A[i])
    L_a = len(divisors_a)
    cnt = set()
    #cnt_2 = [0 for i in range(L_a)]
    #採択する約数
    for i in range(L_a):
        d = divisors_a[i]
        if d in divs:
            cnt.add(d)
            #cnt_2[i] += 1
        divs.add(d)
    #倍数列挙
    #倍数の個数を数える
    dp = [0 for i in range(L_a)]
    top_div = set()
    mother = 1
    grand_mother = 1
    for i in range(L_a):
        if not (divisors_a[i]) in cnt:
            continue
        chk = True
        for j in range(i+1, L_a):
            if divisors_a[j] in cnt and divisors_a[j] % divisors_a[i] == 0:
                #print(divisors_a[i],divisors_a[j])
                chk = False
                break
        if chk:
            top_div.add(divisors_a[i])
    #print(top_div)
    L_d = len(top_div)
    for k in range(1,L_d+1):
        for comb in combinations(top_div, k):
            t = 0
            for c in comb:
                t = math.gcd(t,c)
            if k&1:
                mother *= repyu[t]
            else:
                grand_mother *= repyu[t]
    #print(grand_mother)
    #print(mother)
    ans *= grand_mother*pow(mother, -1, mod)%mod
    ans %= mod
    print(ans)