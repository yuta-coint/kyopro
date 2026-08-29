N,L=map(int,input().split())
A = list(map(int,input().split()))
r = N-1
ans = float("inf")
for l in range(N):
    while True:
        if r==-1:
            break
        ans = min(ans,abs(A[l]+A[r]-L))
        if A[l]+A[r]>L:
            r-=1
        else:
            break
print((L+ans)*2)