N,M = map(int,input().split())
A = list(map(int,input().split()))
cnt = 0
for i in range(1,N+1):
    print(A[cnt]-i)
    if A[cnt]==i:
        cnt+=1
