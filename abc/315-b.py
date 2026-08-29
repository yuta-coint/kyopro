S = list(input())
ans = []
for i in S:
    if i in "aiueo":
        continue
    ans.append(i)
print(*ans,sep="")