import sys
from functools import lru_cache

input = sys.stdin.readline
sys.setrecursionlimit(200000)

@lru_cache(maxsize=None)
def generalized_floor_sum(n, m, a, b):
    a1, a2 = a // m, a % m
    b1, b2 = b // m, b % m
    k = (a2 * (n - 1) + b2) // m
    s_01 = n * (n - 1) // 2 * a1 + b1 * n
    s_11 = n * (n - 1) // 2 * b1 + n * (2 * n - 1) * (n - 1)//6 * a1
    s_02 = n * (n - 1) * (2 * n - 1)//6 * a1 * a1 + n * (n - 1) * a1 * b1 + n * b1 * b1 + 2 * a1 * n * (n - 1) // 2  * k + 2 * b1 * n * k
    if a2 == 0:
        return s_01, s_11, s_02
    gfs_01, gfs_11, gfs_02 = generalized_floor_sum(k, a2, m, m + a2 - b2 - 1)
    return s_01 + n * k - gfs_01, s_11 + n * (n - 1) // 2  * k + (gfs_01 - gfs_02)//2, s_02 + n * k * k + (- 2 * b1 - 1 + a1) * gfs_01 - 2 * gfs_11 - a1 * gfs_02

T = int(input())
for _ in range(T):
    N,M,A,B1,B2 = map(int,input().split())
    if B1 > B2:
        B1, B2 = B2, B1
    ans = A * A * N * (N - 1) * (2 * N - 1)// 6 + (B1 + B2) * A * N * (N - 1) // 2 + B1 * B2 * N
    ans *= 2
    gfsb1_01, gfsb1_11, gfsb1_02 = generalized_floor_sum(N, M, A, B1)
    gfsb2_01, gfsb2_11, gfsb2_02 = generalized_floor_sum(N, M, A, B2)
    ans -= 2 * A * M * gfsb1_11
    ans -= 2 * A * M * gfsb2_11
    ans += (M * M - 2 * B2 * M )* gfsb1_01
    ans += (- 2 * B1 * M - M * M) * gfsb2_01
    ans += M * M * gfsb1_02
    ans += M * M * gfsb2_02
    print(ans//2)
    generalized_floor_sum.cache_clear()