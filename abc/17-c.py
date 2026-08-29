n,m = map(int,input().split())
score = [0 for i in range(m+1)]
sumscore = [0 for i in range(m)]
alls = 0
for i in range(n):
    l,r,s = map(int,input().split())
    score[l-1]+=s
    score[r]-=s
    alls += s
sumscore[0] = score[0]
for i in range(1,m):
    sumscore[i] = sumscore[i-1]+score[i]
ans = alls-min(sumscore)
print(ans)