S = list(input())
T = list(input())
T = set(T)
ans = "Yes"
for i in range(1,len(S)):
    if 0<=ord(S[i])-ord("A")<26:
        if not (S[i-1] in T):
            ans = "No"
print(ans)