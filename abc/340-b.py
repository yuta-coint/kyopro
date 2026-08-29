Q = int(input())
L = 0
A = []
for i in range(Q):
    n,x = map(int,input().split())
    if n==1:
        A.append(x)
        L+=1
    else:
        print(A[L-x])