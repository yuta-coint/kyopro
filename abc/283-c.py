S = list(input())
ls = len(S)
temp = -1
ans = ls
for i in range(ls):
    if S[i]=="0" and temp=="0":
        ans-=1
        temp = -1
    else:
        temp = S[i]
print(ans)