N,M = map(int,input().split())
A = list(map(int,input().split()))
ans = [(float("inf"),0) for i in range(M+1)]
ans[0]=(0,-1)
for j in range(N):
    for i in reversed(range(1,M+1)):
        if A[j]>i:
            continue
        elif A[j]==i:
            if j==0:
                ans[i]=(0,j)
            else:
                if ans[i][0]!=0:
                    ans[i]=(1,j)
        else:
            if ans[i-A[j]]==(float("inf"),0):
                continue
            if ans[i-A[j]][1]==j-1:
                if ans[i-A[j]][0]<=ans[i][0]:
                    ans[i]=(ans[i-A[j]][0],j)
            else:
                if ans[i-A[j]][0]+1<=ans[i][0]:
                    ans[i]=(ans[i-A[j]][0]+1,j)
    print(ans)
                    
for i in range(1,M+1):
    if ans[i]==(float("inf"),0):
        print(-1)
    else:
        if ans[i][1]==N-1:
            print(ans[i][0])
        else:
            print(ans[i][0]+1)

