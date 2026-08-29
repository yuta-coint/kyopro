N,M = map(int,input().split())
S = [list(input()) for i in range(N)]
T = [list(input()) for i in range(M)]
for a in range(N-M+1):
    for b in range(N-M+1):
        cnt = 0
        for i in range(M):
            for j in range(M):
                if S[a+i][b+j] != T[i][j]:
                    cnt = 1
        if cnt ==0:
            print(a+1,b+1)
            exit()