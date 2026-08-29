N,d = map(int,input().split())
A = [list(map(int,input().split())) for i in range(N)]
ansa = [[] for i in range(N)]
ansb = [[] for i in range(N)]
for i in range(N):
    for j in range(N):
        if (i+j)&1:
            amari = A[i][j]%(2*d)
            if amari<=d:
                ansa[i].append(A[i][j]-amari)
            else:
                ansa[i].append(A[i][j]+2*d-amari)
            ansb[i].append(A[i][j]-amari+d)
        else:
            amari = A[i][j]%(2*d)
            if amari<=d:
                ansb[i].append(A[i][j]-amari)
            else:
                ansb[i].append(A[i][j]+2*d-amari)
            ansa[i].append(A[i][j]-amari+d)
costa = 0
costb = 0
for i in range(N):
    for j in range(N):
        costa+=abs(A[i][j]-ansa[i][j])
        costb+=abs(A[i][j]-ansb[i][j])
print(costa,costb)
if costa<costb:
    for i in range(N):
        print(*ansa[i])
else:
    for i in range(N):
        print(*ansb[i])