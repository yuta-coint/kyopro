N=int(input())
events = [tuple(map(int,input().split())) for i in range(N)]
ans = []
needs = [0 for i in range(N)]
have = 0
kmin = 0
for i in reversed(range(N)):
    t,x = events[i]
    x-=1
    if t==1:
        if needs[x]>0:
            needs[x]-=1
            have-=1
            ans.append(1)
        else:
            ans.append(0)
    else:
        needs[x]+=1
        have+=1
    if kmin<have:
        kmin = have
if sum(needs)==0:
    print(kmin)
    ans.reverse()
    print(*ans)
else:
    print(-1)