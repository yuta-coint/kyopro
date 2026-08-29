N = int(input())
A = [input() for i in range(N)]
ans = 1
for i in range(N):
    for j in range(N):
        if A[i][j]=="-" or A[j][i]=="-":
            continue
        if A[i][j]=="W":
            if A[j][i]!="L":
                ans = 0
        if A[i][j]=="L":
            if A[j][i]!="W":
                ans = 0
        if A[i][j]=="D":
            if A[j][i]!="D":
                ans = 0
if ans ==1:
    print("correct")
else:
    print("incorrect")
             
