R,G,B,K = map(int,input().split())
X,Y,Z = map(int,input().split())
mod = 998244353
poly_R  = []
poly_G  = []
poly_B  = []
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
def convolve2(f,g,p):
    f1,f2 = np.divmod(f,1<<15)
    g1,g2 = np.divmod(g,1<<15)
    a = convolve(f1,g1)%p
    c = convolve(f2,g2)%p
    b=  (convolve(f1+f2,g1+g2)-(a+c))%p
    h = (a<<30)+(b<<15)+c
    return h%p
key = 1
for i in range(R+1):
    if i<K-Y:
        poly_R.append(0)
    else:
        poly_R.append(key)
    key *= R-i
    key %=mod
    key *= pow(i+1,mod-2,mod)
    key%=mod
key = 1
for i in range(G+1):
    if i<K-Z:
        poly_G.append(0)
    else:
        poly_G.append(key)
    key *= G-i
    key %=mod
    key *= pow(i+1,mod-2,mod)
    key%=mod
key = 1
for i in range(B+1):
    if i<K-X:
        poly_B.append(0)
    else:
        poly_B.append(key)
    key *= B-i
    key %=mod
    key *= pow(i+1,mod-2,mod)
    key%=mod
#print(poly_R,poly_G,poly_B)
RG = convolve2(poly_R,poly_G,mod)
lRG = len(RG)
RGB = 0
for i in range(K+1):
    if i>=lRG or K-i>=B+1:
        continue
    RGB+=RG[i]*poly_B[K-i]%mod
    RGB%=mod
print(RGB)
