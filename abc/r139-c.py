N,M = map(int,input().split())
if N<M:
    flag = 0
else:
    N,M = M,N
    flag = 1
ans = []
for i in range(N):
    if i&1:
        for t in range(3):
            if 1<=i+t<=M:
                ans.append((i+1,i+t))
    else:
        for t in range(5):
            if 1<=i-1+t<=M:
                ans.append((i+1,i-1+t))
if N&1:
    if M>=N+3:
        for j in range(N+3,M+1):
            ans.append((N,j))
else:
    if M>=N+2:
        for j in range(N+2,M+1):
            ans.append((N,j))
print(len(ans))
for i,j in ans:
    if flag==0:
        print(*(i,j))
    else:
        print(*(j,i))