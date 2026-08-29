from ast import While

from sympy import C


N,K = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
ca = True
cb = True
for i in range(1,N):
    tca = False
    tcb = False
    if ca:
        if abs(A[i-1]-A[i])<=K:
            tca = True
        if abs(A[i-1]-B[i])<=K:
            tcb = True
    if cb:
        if abs(B[i-1]-A[i])<=K:
            tca = True
        if abs(B[i-1]-B[i])<=K:
            tcb = True
    ca = tca
    cb = tcb
if ca or cb:
    print("Yes")
else:
    print("No")
