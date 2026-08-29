n = int(input())
ans = [0 for i in range(5001)]
jobs = [list(map(int,input().split())) for i in range(n)]
jobs.sort()
for i in range(n):
    d = jobs[i][0]
    c = jobs[i][1]
    s = jobs[i][2]
    if c>d:
        continue
    for j in reversed(range(c,d+1)):
        ans[j] = max(ans[j-c]+s,ans[j])
    for j in range(j+1,5001):
        ans[j] = max(ans[j],ans[j-1])
print(max(ans))

