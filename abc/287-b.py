N,M = map(int,input().split())
check = set()
check = [0 for i in range(N)]
S = [input()[3:] for i in range(N)]
ans = 0
for i in range(M):
    T = input()
    for j in range(N):
        if S[j]==T:
            check[j]=1
print(sum(check))
