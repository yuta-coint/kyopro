T = int(input())
for _ in range(T):
    N,W = map(int,input().split())
    ans = 0
    omomi = [[] for i in range(60)]
    for i in range(N):
        x,y = map(int,input().split())
        omomi[x].append(y)
    for i in range(60):
        omomi[i].sort()
        L = len(omomi[i])
        if i == 59:
            break
        if W&1:
            if L>0:
                ans += omomi[i].pop()
                L-=1
        #print(L,len(omomi[i]))
        for j in range(L//2):
            #print(j,L,2*j+(L&1)+1)
            omomi[i+1].append(omomi[i][2*j+(L&1)]+omomi[i][2*j+(L&1)+1])
        if L&1:
            omomi[i+1].append(omomi[i][0])
        W //= 2
    for i in range(min(W,L)):
        ans += omomi[-1].pop()
    print(ans)