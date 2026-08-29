S = list(input())
ans = 0
atc = "atcoder"
ch = {i:atc[i] for i in range(7)}
ans = 0
for i in range(7):
    id = S.index(ch[i])
    for j in reversed(range(i,id)):
        S[j],S[j+1] = S[j+1],S[j]
        ans+=1
        #print(S)
print(ans)