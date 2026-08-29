N = int(input())
P = [0]+list(list(map(int,input().split())))
ans = []
cnt = 1
for i in range(1,N+1,2):
    t = i
    if P[i]%2==1:
        while t>cnt:
            ans.append(("B",t-2))
            P[t],P[t-2]=P[t-2],P[t]
            t-=2
        cnt+=2
cnt=2
for i in range(2,N+1,2):
    t = i
    if P[i]%2==0:
        while t>cnt:
            ans.append(("B",t-2))
            P[t],P[t-2]=P[t-2],P[t]
            t-=2
        cnt+=2
for i in reversed(range(1,N+1)):
    if (P[i]-i)%2!=0:
        P[i],P[i-1]=P[i-1],P[i]
        ans.append(("A",i-1))
for i in range(1,N+1,2):
    t = P.index(i)
    while t>i:
        ans.append(("B",t-2))
        P[t],P[t-2]=P[t-2],P[t]
        t-=2
for i in range(2,N+1,2):
    t = P.index(i)
    while t>i:
        ans.append(("B",t-2))
        P[t],P[t-2]=P[t-2],P[t]
        t-=2
print(len(ans))
for i in ans:
    print(*i)