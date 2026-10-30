T=  int(input())
from math import ceil
for _ in range(T):
    N = int(input())
    S = [0] * N
    for i in range(N):
        #B = 1の場合に帰着できる。偶数だけならBobの勝ち
        A,B = map(int,input().split())
        if A%(B + 1) == 0:
            S[i] = 0
        else:
            S[i] = 1
    if 1 in S:
        print("Alice")
    else:
        print("Bob")