vit = [[],[],[]]
N,X = map(int,input().split())
for i in range(N):
    v,a,c = map(int,input().split())
    vit[v-1].append((a,c))
#iカロリー以下で、どの程度の栄養がえられるか
score = [[0 for i in range(X+1)] for t in range(3)]
for v in range(3):
    for a,c in vit[v]:
        for x in reversed(range(X+1)):
            if x>=c:
                if score[v][x]<score[v][x-c]+a:
                    score[v][x]=score[v][x-c]+a
mi1 = [0 for i in range(X+1)]
for i in range(X+1):
    for j in range(X+1):
        if i+j>X:
            break
        if mi1[i+j]<min(score[0][i],score[1][j]):
            mi1[i+j]=min(score[0][i],score[1][j])
ans = 0
for i in range(X+1):
    if ans<min(score[2][i],mi1[X-i]):
        ans=min(score[2][i],mi1[X-i])
print(ans)