temp = "o"
S = input()
L = len(S)
ans = 0
for i in range(L):
    if S[i]==temp:
        ans+=1
    temp = S[i]
if temp == "i":
    ans+=1
print(ans)