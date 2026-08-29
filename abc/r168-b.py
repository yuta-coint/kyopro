N = int(input())
A = list(map(int,input().split()))
xo=0
for i in range(N):
    xo^=A[i]
if xo!=0:
    print(-1)
    exit()
A.sort(reverse=True)
for i in range(N//2):
    if A[2*i]==A[2*i+1]:
        A[2*i]=0
        A[2*i+1]=0
    else:
        print(A[2*i]-1)
        exit()
print(0)