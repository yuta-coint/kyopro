n = int(input())
s = input()
ans = [n for i in range(n+1)]
l = 0
r = n
for i in range(n):
    if s[i]=="L":
        ans[r]=i
        r-=1
    else:
        ans[l]=i
        l+=1
print(*ans)

