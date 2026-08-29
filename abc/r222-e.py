def fwt(f0):
    k = (len(f0) - 1).bit_length()
    n = 1 << k
    f = f0[:] + [0] * (n - len(f0))
    for i in range(k):
        a = 1 << i
        for j in range(n):
            if a & j: continue
            x = f[j]
            y = f[j|a]
            f[j] = x + y
            f[j|a] = x - y
    return f
def ifwt(f0):
    k = (len(f0) - 1).bit_length()
    n = 1 << k
    f = f0[:] + [0] * (n - len(f0))
    for i in range(k):
        a = 1 << i
        for j in range(n):
            if a & j: continue
            x = f[j]
            y = f[j|a]
            f[j] = x + y >> 1
            f[j|a] = x - y >> 1
    return f

def xor_convolution_a(A, B):
    n = 1 << (max(len(A), len(B)) - 1).bit_length()
    A += [0] * (n - len(A))
    B += [0] * (n - len(B))
    l = [0] * n
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            l[i^j] += a * b
    return l

def xor_convolution(A, k):
    aa = fwt(A)
    g = [pow(a, k, P) for a in aa]
    g = fwt(g)
    h = [a * im % P for a in g]
    return h
def subcalc(a):
    a %= P
    if a == 0: return 0
    if a == 1: return N
    return (pow(a, N, P) - 1) * pow(a - 1, P - 2, P) % P * a % P
def xor_convolution_sum(A, k):
    aa = fwt(A)
    g = [subcalc(a) for a in aa]
    g = fwt(g)
    return g[0] * im % P
N,M = map(int,input().split())
P = 998244353
A = [int(a) for a in input().split()]
m = 1 << M
im = pow(m, P - 2, P)


A = list(map(int,input().split()))
count_A = {}
for i in range(N):
    if A[i] in count_A:
        count_A[A[i]] += 1
    else:
        count_A[A[i]] = 1
sA = set(A)
ans = 0
for t in range(N):
    temp = 0
    old_sA = sA
    sA = set()
    for k in old_sA:
        if count_A[k] > t:
            sA.add(k)
    if max(sA) == -1:
        break
    sA = list(sA)
    X = [0 for i in range(2**M)]
    for 
    temp -= N
    temp *= 499122177
    temp %= P
    ans += temp
    ans %= P
print(ans)