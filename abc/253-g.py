N,L,R = map(int,input().split())
cnt = 0
ans = [i for i in range(N+1)]
ma = N
temp = []
counter = N
for i in range(1,N):
    cntr = cnt+N-i
    ll = i+L-cnt
    rr = i+R-cnt
    #print(ll,rr)
    #両方入っている
    if R<=cntr and cnt<L:
        ans = [t for t in range(N+1)]
        for j in range(ll,rr+1):
            ans[i],ans[j]=ans[j],ans[i]
        break
    #Lだけ入っている
    if cnt<L<=cntr:
        for j in range(ll,N+1):
            ans[i],ans[j]=ans[j],ans[i]
        temp = ans[i+1:]
        ans = ans[:i+1]
    #Rだけ入っている
    if cnt<R<=cntr:
        ans+=temp
        for j in range(i+1,rr+1):
            ans[i],ans[j]=ans[j],ans[i]
    if L<=cnt and cntr<R:
        ans.append(temp.pop())    
    cnt+=N-i
print(*ans[1:])



