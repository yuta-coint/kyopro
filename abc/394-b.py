N = int(input())
S = []
for i in range(N):
    s = input()
    S.append((len(s),s))
S.sort()
ans = []
for i in range(N):
    ans.append(S[i][1])
print(*ans,sep="")
