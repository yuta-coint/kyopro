S = list(input())
T=  list(input())
lt=  len(T)
ls = len(S)
ans = "No"
if ls<lt:
    print(ans)
    exit()
for i in range(ls-lt+1):
    for j in range(i,i+lt):
        if S[j]!=T[j-i]:
            break
    else:
        ans = "Yes"
print(ans)
