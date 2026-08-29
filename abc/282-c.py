inout = 0
N = int(input())
S = list(input())
for i in range(N):
    if S[i]=='"':
        inout = 1-inout
    elif S[i]=="," and inout==0:
        S[i]="."
print(*S,sep="")