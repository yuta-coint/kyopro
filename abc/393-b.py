S = input()
L = len(S)
ans = 0
for i in range(L):
    if S[i]!="A":
        continue
    for sukima in range(1,L):
        if i+sukima*2>=L:
            continue
        if S[i+sukima]=="B" and S[i+sukima*2] == "C":
            ans+=1
print(ans)