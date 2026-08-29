from math import isqrt
def sieve_of_eratosthenes(n):
    prime = [True for i in range(n+1)]
    prime[0] = False
    prime[1] = False

    sqrt_n = isqrt(n)
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
List_of_primes = sieve_of_eratosthenes(2*(10**5))
set_of_primes = set(List_of_primes)
mod=998244353
N, M = map(int,input().split())
sqrtN = isqrt(N)
def Lucy_dp(N):
    sqrtN = isqrt(N)
    S_small = [0 for i in range(sqrtN + 1)]
    sqrtN2 = N//(sqrtN + 1)
    S_large = [0 for i in range(sqrtN2 + 1)]
    S1_small = [0 for i in range(sqrtN + 1)]
    S1_large = [0 for i in range(sqrtN2 + 1)]
    S2_small = [0 for i in range(sqrtN + 1)]
    S2_large = [0 for i in range(sqrtN2 + 1)]
    for i in range(2,sqrtN + 1):
        S_small[i] = M * (i - 1) % mod
        S1_small[i] = M*(max(0,i - 1)//3) % mod
        S2_small[i] = M*((i + 1)//3) % mod
    for i in range(1,sqrtN2 + 1):
        j = N // i
        if j <= 1:
            continue
        S_large[i] = M * (j - 1) % mod
        S1_large[i] = M*(max(0,j - 1)//3) % mod
        S2_large[i] = M*((j + 1)//3) % mod
    for x in range(2,sqrtN + 1):
        if x == 1:
            continue
        if not (x in set_of_primes):
            continue
        for i in range(1, sqrtN2 + 1):
            n = N// i
            if n < x * x:
                break
            if n // x <= sqrtN:
                S_large[i] -= S_small[n // x]
            else:
                S_large[i] -= S_large[i * x]
            S_large[i] += S_small[x - 1]
            S_large[i] %= mod
            if x % 3 == 1:
                if n // x <= sqrtN:
                    S1_large[i] += -S1_small[n // x] + S1_small[x - 1]
                    S2_large[i] += -S2_small[n // x] + S2_small[x - 1]
                else:
                    S1_large[i] += -S1_large[i * x] + S1_small[x - 1]
                    S2_large[i] += -S2_large[i * x] + S2_small[x - 1]
            elif x % 3 == 2:
                if n // x <= sqrtN:
                    S1_large[i] += -S2_small[n // x] + S2_small[x - 1]
                    S2_large[i] += -S1_small[n // x] + S1_small[x - 1]
                else:
                    S1_large[i] += -S2_large[i * x] + S2_small[x - 1]
                    S2_large[i] += -S1_large[i * x] + S1_small[x - 1]
            S1_large[i] %= mod
            S2_large[i] %= mod
        for i in reversed(range(2, sqrtN + 1)):
            if i < x * x:
                break
            S_small[i] -= S_small[i // x]
            S_small[i] += S_small[x - 1]
            S_small[i] %= mod
            if x % 3 == 1:
                S1_small[i] += -S1_small[i // x] + S1_small[x - 1]
                S2_small[i] += -S2_small[i // x] + S2_small[x - 1]
            elif x % 3 == 2:
                S1_small[i] += -S2_small[i // x] + S2_small[x - 1]
                S2_small[i] += -S1_small[i // x] + S1_small[x - 1]
            S1_small[i] %= mod
            S2_small[i] %= mod
    for i in range(2,sqrtN + 1):
        if i >= 3:
            S1_small[i] += M
            S2_small[i] += M
    for i in range(1,sqrtN2 + 1):
        j = N // i
        if j >= 3:
            S1_large[i] += M
            S2_large[i] += M
    return S_small, S_large, S1_small, S1_large
#リストにする。
F_prime_small,F_prime_large,G_prime_small,G_prime_large = Lucy_dp(N)


#素因数の個数とgの関係
g_k = [1]
for i in range(1,80):
    g_k.append(g_k[-1] * (M - 1 + i) % mod * pow(i, -1, mod) % mod)
def search_f_prime(x, mode):
    if mode:
        if x <= sqrtN:
            return F_prime_small[x]
        else:
            return F_prime_large[N // x]
    else:
        if x <= sqrtN:
            return G_prime_small[x]
        else:
            return G_prime_large[N // x]
#素因数pkに対するf(pk^e)の計算
def calc_f(pk, e, mode):
    ans = g_k[e]
    #σ(p e)mod3=0の判定
    if mode == False:
        if pk % 3 == 1:
            if (e + 1) % 3 == 0:
                ans = 0
        elif pk % 3 == 2:
            if e % 2 == 1:
                ans = 0
    return ans

def black_algorithm(mode):
    ans  = 0
    stack = []
    id_pk = 0
    pk = List_of_primes[id_pk]
    while pk * pk <= N:
        stack.append((1, id_pk, 1))
        id_pk += 1
        pk = List_of_primes[id_pk]
    stack.reverse()
    #「最大の素数を抜いたもの」ごとに計算を行う。気持ちとしてはp^{k}倍の辺を伸ばしていくイメージn×p_k^{e}を探索する。
    ans = search_f_prime(N,mode)
    while stack:
        #ベース、次にかける素数、f(n)の値
        n, id_pk, f_n = stack.pop()
        pk = List_of_primes[id_pk]
        n_times_pk = n * pk
        pk_count = 1
        while n_times_pk * pk <= N:
            #n_times_pkについて計算を行う。
            #print(n_times_pk)
            new_f_n = f_n * calc_f(pk, pk_count, mode) % mod
            ans += (search_f_prime(N // n_times_pk,mode) - search_f_prime(List_of_primes[id_pk],mode)) * new_f_n % mod
            ans += f_n * calc_f(pk, pk_count + 1, mode) % mod
            ans %= mod
            #n_times_pkから始まる枝をスタックに追加する。
            new_id_pk = id_pk
            new_id_pk += 1
            new_pk = List_of_primes[new_id_pk]
            while n_times_pk * new_pk * new_pk <= N:
                stack.append((n_times_pk, new_id_pk,new_f_n))
                new_id_pk += 1
                new_pk = List_of_primes[new_id_pk]
            #次のべきに遷移
            n_times_pk *= pk
            pk_count += 1
    return ans
T = black_algorithm(True)
F = black_algorithm(False)
final_ans = (T - F) % mod
print(final_ans)