N,M = map(int,input().split())
A = [0]+list(map(int,input().split()))
C = [0]+list(map(int,input().split()))
X = list(map(int,input().split()))
#i個目までをj個弾くためのコスト
cost = [[0 for j in range(N+1)] for i in range(N+1)]
X = set(X)
for i in range(N+1):
    for j in range(N+1):
        if i<j:
            cost[i][j]=10**16
ban = 0
for i in range(1,N+1):
    if ban==1:
        cost[i][0]=10**16
    Ls = [10**9]
    for j in reversed(range(i+1)):
        if C[j]<Ls[-1]:
            Ls.append(C[j])
        else:
            Ls.append(Ls[-1])
    #print(Ls)
    if i in X:
        for j in range(1,i+1):
            cost[i][j] = cost[i-1][j-1]+Ls[j]+A[i]
        ban=1
        cost[i][0]=10**16
        continue
    for j in range(1,i+1):
        cost[i][j]=cost[i-1][j]
        temp = cost[i-1][j-1]+Ls[j]+A[i]
        if cost[i][j]>temp:
            cost[i][j]=temp
ans = 10**16
#print(cost)
print(min(cost[N]))