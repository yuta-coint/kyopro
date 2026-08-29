N = int(input())
S = [list(input()) for i in range(N)]
from copy import copy
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        T = S[i]+S[j]
        T2 = copy(T)
        T2.reverse()
        if T==T2:
            print("Yes")
            exit()
print("No")