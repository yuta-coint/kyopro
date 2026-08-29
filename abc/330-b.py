N,L,R = map(int,input().split())
A = list(map(int,input().split()))
for x in A:
    if x>R:
        print(R)
    elif x<L:
        print(L)
    else:
        print(x)