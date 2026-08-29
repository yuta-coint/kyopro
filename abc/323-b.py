N = int(input())
sq = []
for i in range(N):
    S = input()
    sq.append((-S.count("o"),i))
sq.sort()
ans = [sq[i][1]+1 for i in range(N)]
print(*ans)