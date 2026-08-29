N = int(input())
check = [False for i in range(N)]
rank = 0
S = input()
for i in range(N):
    if S[i]=="(":
        rank+=1
    elif S[i]==")":
        if rank==0:
            check[i]=True
        else:
            rank-=1
    else:
        if rank==0:
            check[i]=True
rank = 0
for i in reversed(range(N)):
    if S[i]==")":
        rank+=1
    elif S[i]=="(":
        if rank==0:
            check[i]=True
        else:
            rank-=1
    else:
        if rank==0:
            check[i]=True
ans = []
for i in range(N):
    if check[i]:
        ans.append(S[i])
print(*ans,sep="")