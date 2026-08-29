N = int(input())
a = list(map(int,input().split()))
sum_a = [0]
for i in range(N):
    sum_a.append(sum_a[-1]+a[i])
ans = [[10**24 for i in range(N+1)] for j in range(N+1)]
for width in range(1,N+1):
    for i in range(N+1-width):
        j = i+width
        if width==1:
            ans[i][i+width]=0
            continue
        s = sum_a[j]-sum_a[i]
        for k in range(i+1,j):
            if ans[i][j]>ans[i][k]+ans[k][j]+s:
                ans[i][j]=ans[i][k]+ans[k][j]+s
print(ans[0][N])