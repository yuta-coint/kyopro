N = int(input())
path = [[False for i in range(N)] for j in range(N)]
word = [input() for i in range(N)]
for i in range(N):
    for j in range(N):
        if i==j:
            continue
        if word[i][-1]==word[j][0]:
            path[i][j]=True
TSP = [[0 for pat in range(2**N)] for i in range(N)]
#すでに訪れている場所たち
for pat in reversed(range(2**N)):
    #i:現在地
    for i in range(N):
        if (pat>>i)&1==0:
            continue
        #一歩進んでLOSEがあるか
        for j in range(N):
            if i==j:
                continue
            if (pat>>j)&1:
                continue
            if path[i][j] and TSP[j][pat+(1<<j)]==0:
                TSP[i][pat]=1
ans = "Second"
for i in range(N):
    if TSP[i][1<<i]==0:
        ans = "First"
print(ans)
