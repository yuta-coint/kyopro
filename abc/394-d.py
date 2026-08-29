S = input()
L = len(S)
C = 0
stk = []
for i in range(L):
    if C>0:
        if (S[i],stk[C-1]) in [(">","<"),(")","("),("]","[")]:
            stk.pop()
            C-=1
        else:
            stk.append(S[i])
            C+=1
    else:
        stk.append(S[i])
        C+=1
if C==0:
    print("Yes")
else:
    print("No")