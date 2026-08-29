import sys
input = sys.stdin.readline
def factorization(numa):
    arr = []
    hp = numa
    for i in range(2, int(-(-numa**0.5//1))+1):
        powa = 0
        while hp%i==0:
            hp //= i
            arr.append(i)
    if hp>1:
        arr.append(hp)
    return(set(arr))
def divisors(m):
    div = []
    for i in range(1, int(-(-m**0.5//1))+1):
        if m%i==0:
            div.append(i)
            if i!= m//i:
                div.append(m//i)
    div = set(div)
    div = list(div)
    return(sorted(div))
def divisors2(m):
    div = []
    for i in fac:
        if m%i==0:
            div.append(i)
            if i!= m//i:
                div.append(m//i)
    return(set(div))
N,P = map(int,input().split())
fac = divisors(P-1)
cnt = {}
for q in fac:
    cnt[q] = 0
A = list(map(int,input().split()))
#各元の位数を計算する。
primes = factorization(P-1)
for i in range(N):
    f = P-1
    for p in primes:
        while f%p==0:
            if pow(A[i],f//p,P)==1:
                f//=p
            else:
                break
    cnt[f]+=1
#割り切れる二つの数の組み合わせを調べる。
ans = 0
for f in fac:
    divs =divisors2(f)
    temp = 0
    for di in divs:
        temp += cnt[di]
    ans += cnt[f]*temp
print(ans)