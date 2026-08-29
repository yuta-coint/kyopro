N = int(input())
A = list(map(int,input().split()))
ans = []
allsum = (3**N-1)//2
for dim in range(N):
    for phase in range(3**dim):
        for i in range(3**(N-dim-1)):
            x,y,z  = phase*(3**(N-dim))+i,phase*(3**(N-dim))+i+(3**(N-dim-1)),phase*(3**(N-dim))+i+2*(3**(N-dim-1))
            A[x],A[y],A[z]=A[y]-A[z],A[x]+A[z]-A[y],A[y]-A[x]
print(*A)
