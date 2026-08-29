N = int(input())
S = list(input())
ans = 0
for i in range(N):
    if S[i]=="b":
        ans+=1<<i
    elif S[i]=="c":
        ans+=1<<(i+1)
print(ans)
