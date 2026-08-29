N = int(input())
taka = 0
aoki = 0
for i in range(N):
    X,Y = map(int,input().split())
    taka+=X
    aoki+=Y
if taka>aoki:
    print("Takahashi")
elif taka<aoki:
    print("Aoki")
else:
    print("Draw")
