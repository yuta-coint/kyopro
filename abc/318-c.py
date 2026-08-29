N,D,P = map(int,input().split())
dp = [0]
F = list(map(int,input().split()))
F.sort(reverse=True)
temp = sum(F)
ans =temp
for i in range(N):
    temp-=F[i]
    if (i+1)%D==0:
        temp+=P
        if ans>temp:
            ans = temp
temp+=P
if ans>temp:
    ans = temp
print(ans)