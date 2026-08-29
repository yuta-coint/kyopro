T = int(input())
for _ in range(T):
    N = int(input())
    X1,Y1 = 0,0
    X2,Y2 = 0,0
    for i in range(N):
        A,B,C = map(int,input().split())
        d1 = min(B,C)
        d2 = min(A,B-d1)
        X1 += d1
        Y1 += d2
        d2  = min(A,B)
        d1 = min(B-d2,C)
        X2 += d1
        Y2 += d2
    if X1 > Y1 and X2 > Y2:
        print(Y2)
    elif X1 < Y1 and X2 < Y2:
        print(X1)
    else:
        print((X1+Y1)//2)
    