N,T = map(int,input().split())
A = list(map(int,input().split()))
loop = sum(A)
T%=loop
ans1 = 0
for i in range(N):
    if T<A[i]:
        ans1 = 1+i
        break
    else:
        T-=A[i]
print(ans1,T)