N,L,R = map(int,input().split())
A = list(map(int,input().split()))
Grundy =0
for i in range(N):
    Grundy^=(A[i]%(L+R))//L
if Grundy==0:
    print("Second")
else:
    print("First")