N,Q = map(int,input().split())
tiles = [input() for i in range(N)]
cum_sum = [[0 for i in range(N+1)] for j in range(N+1)]
for i in range(N):
    for j in range(N):
        cum_sum[i+1][j+1] = cum_sum[i][j+1]+cum_sum[i+1][j]-cum_sum[i][j]
        if tiles[i][j]=="B":
            cum_sum[i+1][j+1]+=1
#座標(X,Y)を右下とすると…
def solve(X,Y):
    ans = (X//N)*(Y//N)*cum_sum[N][N]
    ans += (X//N)*cum_sum[N][Y%N]
    ans += (Y//N)*cum_sum[X%N][N]
    ans += cum_sum[X%N][Y%N]
    return ans
for i in range(Q):
    A,B,C,D = map(int,input().split())
    print(solve(C+1,D+1)-solve(A,D+1)-solve(C+1,B)+solve(A,B))