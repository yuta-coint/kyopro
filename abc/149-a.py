N,M = map(int,input().split())
pow10 = [1%M]
for i in range(N-1):
    pow10.append((pow10[-1]*10+1)%M)
ans = -1
flag=1
for i in reversed(range(N)):
    for j in reversed(range(1,10)):
        if pow10[i]*j%M==0:
            ans = (i,j)
            flag=1
            break
    if flag==1:
        break
if ans ==-1:
    print(-1)
else:
    p = [ans[1] for i in range(ans[0]+1)]
    print(*p,sep="")

