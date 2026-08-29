N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
import numpy as np
def convolve(f, g):
    """多項式 f, g の積を計算する。

    Parameters
    ----------
    f : np.ndarray (int64)
        f[i] に、x^i の係数が入っている

    g : np.ndarray (int64)
        g[i] に、x^i の係数が入っている


    Returns
    -------
    h : np.ndarray
        f,g の積
    """
    # h の長さ以上の n=2^k を計算
    fft_len = 1
    while 2 * fft_len < len(f) + len(g) - 1:
        fft_len *= 2
    fft_len *= 2

    # フーリエ変換
    Ff = np.fft.rfft(f, fft_len)
    Fg = np.fft.rfft(g, fft_len)

    # 各点積
    Fh = Ff * Fg

    # フーリエ逆変換
    h = np.fft.irfft(Fh, fft_len)

    # 小数になっているので、整数にまるめる
    h = np.rint(h).astype(np.int64)

    return h[:len(f) + len(g) - 1]
r = sum(A)+sum(B)
ans = [0 for i in range(N)]
A = A+A
B.reverse()
for b in reversed(range(5)):
    f = np.array([(A[i]>>b)&1 for i in range(2*N)],np.int)
    g = np.array([(B[i]>>b)&1 for i in range(N)],np.int)
    h = convolve(f,g)
    for i in range(N):
        ans[i]+=h[i+N-1]<<b
print(r-min(ans))