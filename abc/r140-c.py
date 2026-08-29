N,X = map(int,input().split())
if (N+1)//2==X:
    ans = [X]
    for i in range(1,N):
        if i&1:
            X+=i
        else:
            X-=i
        ans.append(X)
elif N==2*(X-1):
    ans = [X]
    for i in range(1,N):
        if i&1:
            X-=i
        else:
            X+=i
        ans.append(X)
else:
    ans = [X]
    if X<=N//2:
        Y = N//2+1
    else:
        Y =  N//2
    ans.append(Y)
    i=1
    t = 0
    while i<N:
        if (i+t)&1:
            Y+=i
        else:
            Y-=i
        if Y==X:
            if X<=N//2:
                Y-=1
            else:
                Y+=1
            i+=1
            t=1
        if 1<=Y<=N:
            ans.append(Y)
        else:
            break
        i+=1
print(*ans)


