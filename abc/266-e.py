N=int(input())
ans = 3.5
for i in range(1,N):
    temp = 0
    for x in range(1,7):
        if x>ans:
            temp+=x
        else:
            temp+=ans
    ans = temp/6
print(ans)