import numpy as np
import sys

# 再帰上限を増やす（念のため）
sys.setrecursionlimit(2000000)

mod = 998244353
g = 3             # 法 mod の原始根 (Primitive root)

# --- NTT本体 ---

def ntt(a, mod, root):
    """
    数論変換 (Number Theoretic Transform)
    a: 多項式の係数リスト (長さは2の冪乗であること)
    root: 1の原始N乗根 ω またはその逆元 ω^-1
    """
    n = len(a)
    
    # バタフライ演算のためのビット反転
    h = 0
    while (1 << h) < n:
        h += 1
    for i in range(n):
        j = 0
        for k in range(h):
            if (i >> k) & 1:
                j |= (1 << (h - 1 - k))
        if i < j:
            a[i], a[j] = a[j], a[i]

    # バタフライ演算
    # length はバタフライ演算の「羽の長さ」（ブロックサイズの半分）
    length = 1
    while length < n:
        # ここで length を更新せず、現在の length に対して計算を行う
        
        # 1の原始 (2*length) 乗根
        # w_m^length = -1 (mod p) となる数
        w_m = pow(root, (mod - 1) // (2 * length), mod)
        
        for j in range(0, n, 2 * length):
            w = 1
            for k in range(length):
                # Cooley-Tukey Butterfly
                # u = a[j+k], t = a[j+k+length] * w
                # a[j+k] = u + t
                # a[j+k+length] = u - t
                
                t = (a[j + k + length] * w) % mod
                u = a[j + k]
                
                a[j + k] = (u + t) % mod
                a[j + k + length] = (u - t + mod) % mod
                w = (w * w_m) % mod
        
        # 次のステージへ（長さを倍にする）
        length *= 2
        
    return a

# --- 多項式乗算 (NTTベース) ---

def polynomial_multiplication_fp(A, B, p):
    """
    F_p上の多項式の積をNTTで計算する。
    """
    # 入力をリストに変換
    A = list(A)
    B = list(B)
    
    n_a = len(A)
    n_b = len(B)
    
    # 積の係数の数
    degree_sum = n_a + n_b - 1
    
    # NTTサイズ N は degree_sum 以上の 2の冪
    N = 1
    while N < degree_sum:
        N *= 2
    
    # 係数をNにパディング
    A.extend([0] * (N - n_a))
    B.extend([0] * (N - n_b))

    # 1. NTTを実行
    ntt(A, p, g)
    ntt(B, p, g)
    
    # 2. 周波数領域で乗算
    C = [(A[i] * B[i]) % p for i in range(N)]
    
    # 3. 逆NTTを実行
    # 逆元の計算
    inv_g = pow(g, -1, p)
    inv_N = pow(N, -1, p)
    
    ntt(C, p, inv_g)
    
    # 4. 逆NTTの結果を N^-1 で割る
    result_coeffs = [(C[i] * inv_N) % p for i in range(degree_sum)]
    
    return np.array(result_coeffs, dtype=np.int64)

def inv_of_FPS(fps, n):
    # fps: list of coefficients of the formal power series
    # n: number of terms to compute in the inverse series
    
    # 入力FをNumPy配列に統一
    F = np.asarray(fps[:n], dtype=np.int64)
    
    # 定数項が0の場合は逆元が存在しない
    if F[0] == 0:
        raise ValueError("Constant term cannot be zero.")

    # 1項のみの逆元から始める (長さ k=1)
    inv_fps = np.array([pow(int(F[0]), -1, mod)], dtype=np.int64)
    
    k = 1  # 現在の逆元の長さ

    # k < n となるまで、kを倍にしながら計算
    while k < n:
        
        k_next = min(2 * k, n)
        
        # 1. T = F * G_k (mod x^(k_next)) を計算
        T = polynomial_multiplication_fp(F[:k_next], inv_fps[:k], mod)[:k_next]
        
        # 2. H = 2 - T (mod x^(k_next)) を計算
        H = np.zeros(k_next, dtype=np.int64)
        
        # H[0] = (2 - T[0]) % mod
        H[0] = (2 - T[0]) % mod
        
        # H[i] = (0 - T[i]) % mod for i > 0
        H[1:] = (mod - T[1:]) % mod
        
        # 3. G_next = G_k * H (mod x^(k_next)) を計算
        G_next = polynomial_multiplication_fp(inv_fps[:k], H, mod)[:k_next]
        
        # inv_fps を G_next で更新
        inv_fps = G_next
        
        # 現在の長さを次の長さ k_next に更新
        k = k_next
        
    return inv_fps.tolist()

# --- メイン処理 ---
try:
    # input() の高速化
    input = sys.stdin.readline
    
    line1 = input().strip()
    if not line1:
        sys.exit(0)
    N = int(line1)
    
    line2 = input().strip()
    if not line2:
        A = np.array([])
    else:
        A = np.array(list(map(int, line2.split())))
        
    B = inv_of_FPS(A, N)
    print(*B)
except ValueError as e:
    pass