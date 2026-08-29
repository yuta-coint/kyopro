S = input()
i = int(S[0])
j = int(S[2])
if j < 8:
    x,y = i,j+1
elif i<8 and j == 8:
    x,y = i+1,1
print(*[x,"-",y],sep="")