N,K = map(int,input().split())
A = list(map(int,input().split()))
check = [False for i in range(K+1)]
for i in range(N):
    if A[i]<K:
        check[A[i]]=True
for i in range(K+1):
    if check[i]==False:
        print(i)
        break