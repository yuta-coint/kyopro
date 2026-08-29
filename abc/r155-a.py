from copy import copy
T = int(input())
for case in range(T):
    N,K = map(int,input().split())
    S = list(input())
    K%=2*N
    rS = S.copy()
    rS.reverse()
    if K<N:
        pal = S + rS[N-K:]
        rpal = pal.copy()
        rpal.reverse()
        if pal != rpal:
            print("No")
            continue
        pal = rS[N-K:]+S
        rpal = pal.copy()
        rpal.reverse()
        if pal != rpal:
            print("No")
            continue
        print("Yes")
    else:
        pal = S + rS[:K-N]+rS
        rpal = pal.copy()
        rpal.reverse()
        if pal != rpal:
            print("No")
            continue
        pal = rS[:K-N]+rS+S
        rpal = pal.copy()
        rpal.reverse()
        if pal != rpal:
            print("No")
            continue
        print("Yes")

            
