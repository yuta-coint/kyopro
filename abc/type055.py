N,P,Q = map(int,input().split())
A = list(map(int,input().split()))
from itertools import combinations
ans = 0
for a in range(N-4):
    t1 = A[a]
    for b in range(a+1,N-3):
        t2=t1*A[b]%P
        for c in range(b+1,N-2):
            t3=t2*A[c]%P
            for d in range(c+1,N-1):
                t4=t3*A[d]%P
                for e in range(d+1,N):
                    t5=t4*A[e]%P
                    if t5==Q:
                        ans+=1
print(ans)
