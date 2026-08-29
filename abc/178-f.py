n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
ca =[0 for i in range(n+1)]
cb =[0 for i in range(n+1)]
for i in range(n):
    ca[a[i]]+=1
    cb[b[i]]+=1
a = [[0,0] for i in range(n)]
cnt = 0
safe = True
for i in range(1,n+1):
    if ca[i]+cb[i]>n:
        safe = False
spb = 0
for i in range(1,n+1):
    if ca[i]+cb[i]>spb+n-cnt:
        for _ in range(cb[i]-spb):
            if cnt==n or cb[i]==0:
                break
            a[cnt][1]=i
            cnt+=1
            cb[i]-=1
    if cnt+ca[i]<=n:
        for _ in range(ca[i]):
            a[cnt][0]=i
            spb+=1
            cnt+=1
        ca[i]=0
    if cnt+cb[i]<=n:
        for _ in range(cb[i]):
            a[cnt][1]=i
            cnt+=1
        cb[i]=0
    if cnt+ca[i]>n:
        while cnt<n and ca[i]>0:
            a[cnt][0]=i
            spb+=1
            cnt+=1
            ca[i]-=1
        break
    if cnt+cb[i]>n:
        while cnt<n and cb[i]>0:
            a[cnt][1]=i
            cnt+=1
            cb[i]-=1
        break
rema = []
remb = []
for i in range(1,n+1):
    for _ in range(ca[i]):
        rema.append(i)
    for _ in range(cb[i]):
        remb.append(i)
cnta = 0
cntb = 0
for i in range(n):
    if a[i][0]==0:
        a[i][0]=rema[cnta]
        cnta+=1
    if a[i][1]==0:
        a[i][1]=remb[cntb]
        cntb+=1
a.sort()
ans = [a[i][1] for i in range(n)]
if safe:
    print("Yes")
    print(*ans)
else:    
    print("No")
