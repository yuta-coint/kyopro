N = int(input())
K = list(map(int,input().split()))
S = sum(K)
ans = S
for bits in range(1<<N):
    temp = 0
    for i in range(N):
        if (bits>>i)&1:
            temp+=K[i]
    temp = max(temp,S-temp)
    if ans>temp:
        ans = temp
print(ans)