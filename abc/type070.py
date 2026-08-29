N = int(input())
X = []
Y = []
for i in range(N):
    x,y = map(int,input().split())
    X.append(x)
    Y.append(y)
X.sort()
Y.sort()
ansx = X[N//2]
ansy = Y[N//2]
ans = 0
for i in range(N):
    ans+=abs(ansx-X[i])+abs(ansy-Y[i])
print(ans)
