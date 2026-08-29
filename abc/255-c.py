X,A,D,N = map(int,input().split())
mA = A+(N-1)*D
if mA<A:
    mA,A = A,mA
if X>=mA:
    print(X-mA)
elif X<=A:
    print(A-X)
else:
    print(min((X-A)%abs(D),(A-X)%abs(D)))