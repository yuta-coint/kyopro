

N = int(input())
BIT = [0 for i in range(N+1)]
#i  = 0だとバグる
def add(i,x):
    while i<=N:
        BIT[i]+=x
        i += (i&-i)
#xまでの和をとる
def getSum(x):
    i = x
    gs = 0
    while i>0:
        gs+=BIT[i]
        i -= (i&-i)
    return gs
def inversion_number(X):
    inv_num = 0
    for i in reversed(range(N)):
        inv_num += getSum(X[i]+1)
        add(X[i]+1,1)
    return inv_num
A = list(map(int,input().split()))
B = list(map(int,input().split()))
for i in range(N):
    A[i] += i
    B[i] += i
from copy import copy
E = copy(A)
D = copy(B)
E.sort()
D.sort()
for i in range(N):
    if D[i] != E[i]:
        print(-1)
        exit()
d = {}
cnt = {}
for i in range(N):
    if A[i] in cnt:
        cnt[A[i]] += 1
    else:
        cnt[A[i]] = 1
    d[A[i] *N + cnt[A[i]]] = i
C = [0 for i in range(N)]
cnt2 = {}
for i in range(N):
    if B[i] in cnt2:
        cnt2[B[i]] += 1
    else:
        cnt2[B[i]] = 1
    C[i] = d[B[i] * N + cnt2[B[i]]]
#print(C)
ans = inversion_number(C)
print(ans)