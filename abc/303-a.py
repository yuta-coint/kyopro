N = int(input())
S = list(input())
T = list(input())
for i in range(N):
    if S[i]=="1":
        S[i]="l"
    if S[i]=="0":
        S[i]="o"
    if T[i]=="1":
        T[i]="l"
    if T[i]=="0":
        T[i]="o"
if S==T:
    print("Yes")
else:
    print("No")