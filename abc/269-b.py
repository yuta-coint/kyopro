S = [input() for i in range(10)]
A,B,C,D  = 10,0,10,0
for i in range(10):
    for j in range(10):
        if S[i][j]=="#":
            A = min(i,A)
            B = max(i,B)
            C = min(j,C)
            D = max(j,D)
print(A+1,B+1)
print(C+1,D+1)