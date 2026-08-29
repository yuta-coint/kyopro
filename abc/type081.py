N,K  =map(int,input().split())
check = [[0 for j in range(5001)] for i in range(5001)]
for i in range(N):
    a,b = map(int,input().split())
    check[a][b] +=1
check_sum = [[0 for j in range(5001)] for i in range(5001)]
for i in range(1,5001):
    for j in range(1,5001):
        check_sum[i][j]=check_sum[i-1][j]+check_sum[i][j-1]-check_sum[i-1][j-1]+check[i][j]
ans = 1
for height in range(5001-K):
    for weight in range(5001-K):
        temp = check_sum[height+K][weight+K]-check_sum[height+K][weight]-check_sum[height][weight+K]+check_sum[height][weight]
        if ans<temp:
            ans = temp
print(ans)