X,Y,Z = map(int,input().split())
if X<0:
    X,Y,Z = -X,-Y,-Z
if Y<0 or Y>X:
    print(X)
elif Z<Y:
    print(abs(Z)+abs(Z-X))
else:
    print(-1)
A,B = map(int,input().split())
print(A|B)