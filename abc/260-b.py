N,X,Y,Z = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
chk = [False for i in range(N)]
C = [(-A[i]-B[i],i) for i in range(N)]
A = [(-A[i],i) for i in range(N)]
B = [(-B[i],i) for i in range(N)]
A.sort()
B.sort()
C.sort()
cnt=0
for i in range(X):
    chk[A[i][1]]=True
for i in range(N):
    if cnt==Y:
        break
    if chk[B[i][1]]:
        continue
    chk[B[i][1]]=True
    cnt+=1
cnt=0
for i in range(N):
    if cnt==Z:
        break
    if chk[C[i][1]]:
        continue
    chk[C[i][1]]=True
    cnt+=1
for i in range(N):
    if chk[i]:
        print(i+1)
