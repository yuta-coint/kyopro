N = int(input())
X = list(map(int,input().split()))
X.sort()
print(sum(X[N:4*N])/(3*N))