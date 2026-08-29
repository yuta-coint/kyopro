N = int(input())
S = input()
ans = 0
cnt = 0
for i in range(N-1):
    if S[i]=="<":
        ans+=cnt*(cnt+1)//2
        cnt=0
    else:
        cnt+=1
ans += cnt*(cnt+1)//2
print(ans)