import sys
sys.setrecursionlimit(10 ** 7)
def calc(p, q, N):
    if N == 0:
        return p * q % 998244353
    if N == 1:
        return q * (abs(p - q)) % 998244353
    if N == 2:
        r = abs(p - q)
        s = abs(r - q)
        return (r * s) % 998244353
    if p < 2 * q:
        return calc(q, abs(q - p), N - 1)
    if q == 0:
        return calc(p, q, N % 3)
    t = p//(2 * q)
    if N - 3 * t >= 0:
        return calc(p - 2 * t * q, q, N - 3 * t)
    else:
        s = N // 3
        return calc(p - 2 * s * q, q, N - 3 * s)
N, M, X = map(int, input().split())
ans = 0
for i in range(M + 1):
    c = calc(X, i, N - 2)
    print(c)
    ans += c
    ans %= 998244353
print(ans)

import sys

def calc(p: int, q: int, N: int) -> int:
    while True:
        # ベースケース
        if N == 0:
            return p * q % 998244353
        if N == 1:
            return q * abs(p - q) % 998244353
        if N == 2:
            r = abs(p - q)
            s = abs(r - q)
            return (r * s) % 998244353
        
        # 再帰ステップの反復化
        if p < 2 * q:
            # calc(q, abs(q - p), N - 1)
            p, q, N = q, abs(q - p), N - 1
            continue
            
        if q == 0:
            # calc(p, q, N % 3)
            N %= 3
            continue

        # ユークリッドの互除法的なスキップ処理
        t = p // (2 * q)
        if N - 3 * t >= 0:
            # calc(p - 2 * t * q, q, N - 3 * t)
            p -= 2 * t * q
            N -= 3 * t
        else:
            # calc(p - 2 * s * q, q, N - 3 * s)
            s = N // 3
            p -= 2 * s * q
            N -= 3 * s

def main():
    # 高速な入力読み込み
    tokens = sys.stdin.read().split()
    if not tokens:
        return
    N = int(tokens[0])
    M = int(tokens[1])
    X = int(tokens[2])

    ans = 0
    target_n = N - 2
    
    for i in range(M + 1):
        # 変換した関数を呼び出す
        c = calc(X, i, target_n)
        ans += c
        ans %= 998244353
        
    print(ans)

if __name__ == "__main__":
    main()