N = int(input())
A = list(map(int,input().split()))
big = 10**12
weight = [0 for i in range(N+1)]
for i in reversed(range(N)):
    weight[i]=weight[i+1]+A[i]
temp = [0 for i in range(N)]
pr = 0
mi = 0
for i in range(1,N):
    if weight[i]>0:
        pr=1
    elif weight[i]<0:
        mi=1
if pr^mi==1 and weight[0]==0:
    print("No")
    exit()
print("Yes")
if pr^mi==1:
    for i in range(1,N-1):
        temp[i]=1
    wa = sum(weight[1:N-1])
    if weight[0]>0:
        temp[0]=(-((10**11)//weight[0]))*A[N-1]
    else:
        temp[0]=((10**11)//(-weight[0]))*A[N-1]
    wa+=temp[0]*weight[0]
    #print(wa)
    temp[N-1]=-wa*A[N-1]
    #print(temp)
else:
    temp[0]=0
    for i in range(N-1):
        if weight[N-1]*weight[i]<0:
            temp[i]=(10**11)//abs(weight[i])
            for j in range(i+1,N-1):
                temp[j]=1
            break
        temp[i]=1
    wa = 0
    for i in range(N-1):
        wa+=temp[i]*weight[i]
    temp[N-1]=-wa*A[N-1]    
ans = [temp[0]]
for i in range(1,N):
    ans.append(ans[-1]+temp[i])
print(*ans)

check = 0
for i in range(N):
    check+=ans[i]*A[i]
print(check)