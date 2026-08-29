S = input()
L = len(S)
ans = []
for i in range(L):
    if S[i]=="2":
        ans.append(S[i])
print(*ans,sep="")