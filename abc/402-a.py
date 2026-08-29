S = list(input())
ans = []
for i in range(len(S)):
    if 0<=ord(S[i])-ord("A")<26:
        ans.append(S[i])
print(*ans,sep="")