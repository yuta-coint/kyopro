T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(lambda x:int(x)-1,input().split()))
    ans = 0
    #もともと隣り合っている人は無視する。
    #各人に対して、隣り合っている人の相方が
    black = set()
    for i in range(2*N-1):
        if A[i]==A[i+1]:
            black.add(A[i])
    L = [-1 for i in range(N)]
    R = [-1 for i in range(N)]
    for i in range(2*N):
        if L[A[i]]==-1:
            L[A[i]]=i
        else:
            R[A[i]]=i
    for i in range(N):
        if i in black:
            continue
        if L[i]>0:
            if not (A[L[i]-1] in black):
                if abs(R[A[L[i]-1]]-R[i])==1:
                    ans += 1
        if L[i]<2*N-1:
            if not (A[L[i]+1] in black):
                if abs(R[A[L[i]+1]]-R[i])==1 and L[i]+1!=R[A[L[i]+1]]:
                    ans += 1
    print(ans//2)