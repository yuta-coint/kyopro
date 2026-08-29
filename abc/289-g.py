from collections import deque
deq = deque()
#convex hull trick
#傾きが単調減少になるように辺を追加していき、最小値を求める
#f1とf3の交点がf2より下にあるかを判定する。
def check(f1, f2, f3):
    return (f2[0] - f1[0]) * (f3[1] - f2[1]) >= (f2[1] - f1[1]) * (f3[0] - f2[0])
def f(f1, x):
    return f1[0]*x + f1[1]

# add f_i(x) = a*x + b
def add_line(a, b):
    f1 = (a, b)
    #すでにあるやつで要らないのがないか調べる
    while len(deq) >= 2 and check(deq[-2], deq[-1], f1):
        deq.pop()
    deq.append(f1)

# min f_i(x)
#クエリで与えられるxが単調増加
def query(x):
    while len(deq) >= 2 and f(deq[0], x) >= f(deq[1], x):
        deq.popleft()
    return f(deq[0], x)

N,M = map(int,input().split())
B = list(map(int,input().split()))
C = list(map(int,input().split()))
B.sort(reverse=True)
B = [B[i]*(i+1) for i in range(N)]
#-(i+1)x-B[i]を追加していくが一番大きくなるやつを取ってくるぞ！！
for i in range(N):
    add_line(-(i+1),-B[i])
C = [(C[i],i) for i in range(M)]
C.sort()
ans = [0 for i in range(M)]
for i,j in C:
    ans[j]=-query(i)
print(*ans)