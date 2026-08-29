import array
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
A = array.array('i',[])
from bisect import bisect_left, bisect_right, insort_right
L = 0
def q1(x):
    global L
    insort_right(A,x)
    L+=1
def q2(x,k):
    t = bisect_right(A,x)-1
    if t-k+1<0:
        print(-1)
    else:
        print(rd[A[t-k+1]])
def q3(x,k):
    t = bisect_left(A,x)
    if t+k-1>=L:
        print(-1)
    else:
        print(rd[A[t+k-1]])
Q = int(input())
qL = [list(map(int,input().split())) for i in range(Q)]
a = [qL[i][1] for i in range(Q)]
b = sorted(set(a))
d = {v:i for i, v in enumerate(b)}
rd = {i:v for i, v in enumerate(b)}
for i in range(Q):
    q = qL[i]
    q[1] = d[q[1]]
    if q[0]==1:
        q1(q[1])
    elif q[0]==2:
        q2(q[1],q[2])
    else:
        q3(q[1],q[2])



