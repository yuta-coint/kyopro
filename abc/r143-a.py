ABC=list(map(int,input().split()))
ABC.sort()
A,B,C = ABC[0],ABC[1],ABC[2]
if B+A-C>=0:
    print(C)
else:
    print(-1)