N = int(input())
# N: 処理する区間の長さ
N0 = 2**(N-1).bit_length()
INF = 2**31-1
# a_k の値を x に更新
def update(k, x):
    k += N0-1
    data[k] = x
    while k >= 0:
        k = (k - 1) // 2
        data[k] = min(data[2*k+1], data[2*k+2])
# 区間[l, r)の最小値
def query(l, r):
    L = l + N0; R = r + N0
    s = INF
    while L < R:
        if R & 1:
            R -= 1
            s = min(s, data[R-1])

        if L & 1:
            s = min(s, data[L-1])
            L += 1
        L >>= 1; R >>= 1
    return s
P = list(map(int,input().split()))
for i in range(N):
    P[i]-=1
data = [INF]*(2*N0)
ans = [float("inf") for i in range(N)]
for i in range(N):
    q = query(0,P[i])
    if q-(-i-P[i])<ans[i]:
        ans[i]=i+P[i]+q
    update(P[i],-i-P[i])
data = [INF]*(2*N0)
for i in range(N):
    q = query(P[i],N)
    if q-(P[i]-i)<ans[i]:
        ans[i]=q-(P[i]-i)
    update(P[i],P[i]-i)
data = [INF]*(2*N0)
for i in reversed(range(N)):
    q = query(0,P[i])
    if q-(i-P[i])<ans[i]:
        ans[i]=q-(i-P[i])
    update(P[i],i-P[i])
data = [INF]*(2*N0)
for i in reversed(range(N)):
    q = query(P[i],N)
    if q-(i+P[i])<ans[i]:
        ans[i]=q-(i+P[i])
    update(P[i],i+P[i])
print(*ans)

#各点より右上で大きいやつら
