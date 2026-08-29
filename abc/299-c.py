N = int(input())
S = input()
stock = 0
ans = 0
for i in range(N):
    if S[i]=="o":
        stock+=1
    else:
        stock=0
    if stock>ans:
        ans = stock
if ans == N or ans==0:
    print(-1)
else:
    print(ans)
    