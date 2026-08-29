X,K = map(int,input().split())
for i in range(1,K+1):
    t = X//(10**i)
    mi = t*(10**i)
    ma = (t+1)*(10**i)
    if ma-X > X-mi:
        X = mi
    else:
        X = ma
print(X)