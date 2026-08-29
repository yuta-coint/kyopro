N = int(input())
quizes = [tuple(map(int,input().split())) for i in range(N)]
P = [quizes[i][1] for i in range(N)]
ex = [quizes[i][0]*quizes[i][1] for i in range(N)]
#同じ確率ならでかいのを取りたい
#同じ大きさなら確率高いやつを取りたい
#期待値一緒なら確率高いのを取りたい
exp = []
for i in range(N):
    if ex[i]==0:
        exp.append((10**16,i+1))
    else:
        exp.append(((100-P[i])/ex[i],i+1))
exp.sort()
ans = [exp[i][1] for i in range(N)]
print(*ans)