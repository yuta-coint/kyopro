N,W = map(int,input().split())
a = list(map(int,input().split()))
chk = [0 for i in range(W+1)]
for i in range(N):
    if a[i]<=W:
        chk[a[i]]=1
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if a[i]+a[j]+a[k]<=W:
                chk[a[i]+a[j]+a[k]]=1

for i in range(N-1):
    for j in range(i+1,N):
        if a[i]+a[j]<=W:
            chk[a[i]+a[j]]=1
print(sum(chk))