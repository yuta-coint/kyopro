S = list(input())
ans = 0
for c in S:
    if c=="v":
        ans+=1
    else:
        ans+=2
print(ans)
