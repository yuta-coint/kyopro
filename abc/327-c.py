A = [list(map(int,input().split())) for i in range(9)]
for i in range(9):
    chk1 = [0 for i in range(9)]
    chk2 = [0 for i in range(9)]
    for j in range(9):
        chk1[A[i][j]-1] = 1
        chk2[A[j][i]-1] = 1
    if sum(chk1)!=9 or sum(chk2)!=9:
        print("No")
        exit()
for i in range(3):
    for j in range(3):
        chk = [0 for i in range(9)]
        for k in range(3):
            for l in range(3):
                chk[A[3*i+k][3*j+l]-1] = 1 
        if sum(chk) != 9:
            print("No")
            exit()
print("Yes")