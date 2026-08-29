N,Q = map(int,input().split())
A = list(map(int,input().split()))
A.sort()
S1 = []
S1.append(sum(A))
S2 = []
S2.append(0)
t1 = sum(A)
t2 = 0
for i in range(N):
    t1-=A[i]
    S1.append(t1)
    t2+=A[i]
    S2.append(t2)
#print(A)
for i in range(Q):
    x = int(input())
    m = 0
    M = N
    while m+1<M:
        bis = (m+M)//2
        #print(bis)
        if A[bis]<=x:
            m=bis
        else:
            M=bis
    bis = m+1
    if x<A[0]:
        bis = 0
    print((x*bis-S2[bis])+(S1[bis]-x*(N-bis)))