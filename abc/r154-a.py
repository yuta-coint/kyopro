keta = [1]
mod = 998244353
N = int(input())
#A = ["2" for i in range(10**6)]
#B = ["2" for i in range(10**6)]
A = list(input())
B = list(input())
for i in range(N-1):
    keta.append(keta[-1]*10%mod)
keta.reverse()
first = N
for i in range(N):
    if A[i]!=B[i]:
        if A[i]<B[i]:
            A[i],B[i]=B[i],A[i]
        first=i
        break
if first<N:
    for i in range(first+1,N):
        if A[i]<B[i]:
            A[i],B[i]=B[i],A[i]
x = 0
y = 0
for i in range(N):
    x += int(A[i])*keta[i]%mod
    y+= int(B[i])*keta[i]%mod
    if x>=mod:
        x-=mod
    if y>=mod:
        y-=mod
print(x*y%mod)