D = list(input())
for i in range(len(D)):
    if D[i]=="N":
        D[i]="S"
    elif D[i]=="S":
        D[i]="N"
    elif D[i]=="E":
        D[i]="W"
    elif D[i]=="W":
        D[i]="E"
print(*D,sep="")