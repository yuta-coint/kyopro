S,T,U =  map(int,input().split())
if S*T==U or S*U == T or T*U == S:
    print("Yes")
else:
    print("No")