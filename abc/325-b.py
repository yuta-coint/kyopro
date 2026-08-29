N = int(input())
worker = [tuple(map(int,input().split())) for i in range(N)]
ans = 0
for i in range(24):
    attend = 0
    for w in range(N):
        if 9<=(i+worker[w][1])%24<18:
            attend+=worker[w][0]
    if attend>ans:
        ans = attend
print(ans)