n = int(input())
a = list(map(int,input().split()))
m = 0
M = 10**9+1
while (M-m)*5000>1:
    temp = (m+M)/2
    dpt = [0 for i in range(n+1)]
    dpf = [0 for i in range(n+1)]
    for i in range(n):
        dpt[i+1] = max(dpt[i]+a[i]-temp,dpf[i]+a[i]-temp)
        dpf[i+1] = dpt[i]
    if max(dpt[n],dpf[n])>=0:
        m=temp
    else:
        M=temp
print(m)

m = 0
M = 10**9+1
while m+1<M:
    temp = (m+M)//2
    cnt = 0
    under = 0
    chk = [False for i in range(n)]
    for i in range(n):
        if a[i]>=temp:
            chk[i]=True
            cnt+=1
    f = 0
    for i in range(n):
        if chk[i]:
            f=0
        else:
            if f == 0:
                f=1
            else:
                under+=1
                f=0
    if (cnt+under+1)//2>under:
        m = temp
    else:
        M=temp
print(m)
