#ギャクだと見た。未証明を投げる。
from collections import deque
T = int(input())
for _ in range(T):
    N = int(input())
    S = list(input())
    for i in range(N):
        S[i] = ord(S[i]) - ord("A")
    q = [S[0]]
    L = 1
    for i in range(1,N):
        #print(q)
        if L == 0:
            q.append(S[i])
            L += 1
            continue
        u = S[i]
        while L > 0:
            if q[-1] == u:
                L += 1
                break
            else:
                t = q.pop()
                u = 3 - u - t
                L -= 1
        q.append(u)
    if (N - len(q)) & 1:
        print("Alice")
    else:
        print("Bob")
T = int(input())
for _ in range(T):
    N = int(input())
    A = [0] + list(map(int,input().split()))
    B = [A[i + 1] - A[i] for i in range(N)]
    ans = 0
    for i in range(N - 1, -1,-2):
        ans^= B[i]
    if ans == 0:
        print("Bob")
    else:
        print("Alice")
