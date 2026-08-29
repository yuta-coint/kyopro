N= int(input())
S = [list(input()) for i in range(N)]
answer = [-1 for i in range(2 * N - 1)]
for i in range(N):
    for j in range(N):
        if S[i][j] == "?":
            continue
        p = int(S[i][j])
        if answer[i + j] == -1:
            answer[i + j] = p
        elif answer[i + j] != p:
            print(-1)
            exit()
ans = [[0 for i in range(N)] for j in range(N)]
for i in range(N):
    for j in range(N):
        if answer[i + j] == -1:
            continue
        ans[i][j] = answer[i + j]
for i in range(N):
    print(*ans[i],sep="")