import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
N,Q = map(int,input().split())
A = [0]+list(map(int,input().split()))
dp = [-1 for i in range(8889)]
G_mat = [[0 for j in range(N+1)] for i in range(N+1)]
for i in range(Q):
    X,Y = map(int,input().split())
    G_mat[X][Y]=1
    G_mat[Y][X]=1
dp[0]=[]
def check(chosen,num):
    if num==N+1:
        return 0
    #numを追加できますか？
    for k in chosen:
        if G_mat[k][num]==1:
            break
    else:
        key = A[num]
        for k in chosen:
            key+=A[k]
        if dp[key]==-1:
            dp[key]=chosen+[num]
        else:
            print(len(dp[key]))
            print(*dp[key])
            print(len(chosen+[num]))
            print(*(chosen+[num]))
            exit()
        check(chosen+[num],num+1)
    check(chosen,num+1)
check([],1)