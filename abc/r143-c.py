N,X,Y = map(int,input().split())
A = list(map(int,input().split()))
for i in range(N):
    A[i]%=X+Y
tk = 0
ao = 0
if X<Y:
    for i in range(N):
        if A[i]>=Y:
            ao+=1
        elif A[i]>=X:
            tk+=1
    if tk==0 and ao==0:
        ans=False
    else:
        ans=True
elif X>Y:
    for i in range(N):
        if A[i]>=X:
            tk+=1
        elif A[i]>=Y:
            ao+=1
    if ao>0 or tk==0:
        ans=False
    else:
        ans=True
else:
    cnt=0
    for i in range(N):
        if A[i]>=X:
            cnt+=1
    if cnt==0:
        ans = False
    else:
        ans=True
if ans:
    print("First")
else:
    print("Second")
