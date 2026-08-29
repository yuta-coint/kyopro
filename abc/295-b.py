R,C = map(int,input().split())
B = [list(input()) for i in range(R)]
Bombs = []
for i in range(R):
    for j in range(C):
        if B[i][j]!="#" and B[i][j]!=".":
            Bombs.append((i,j,int(B[i][j])))
for i in range(R):
    temp = []
    for j in range(C):
        if B[i][j]==".":
            temp.append(".")
        else:
            for x,y,b in Bombs:
                if abs(x-i)+abs(y-j)<=b:
                    temp.append(".")
                    break
            else:
                temp.append("#")
    print(*temp,sep="")
