S = list(input())
L = len(S)
for i in reversed(range(1,L)):
    if S[i]=="A" and S[i-1] == "W":
        S[i]="C"
        S[i-1] = "A"
print(*S,sep="")