N = int(input())
S = input()
T = input()
atob = N+1
lefta = N
X = []
for i in reversed(range(N)):
    if S[i]=="A"  and T[i]=="B":
        atob = i
        X.append(i)
    if T[i]=="A":
        lefta = i
btoa = -2
rightb = -1
Y = []
for i in range(N):
    if S[i]=="B" and T[i] == "A":
        btoa = i
        Y.append(i)
    if T[i]=="B":
        rightb = i
if rightb<btoa or lefta>atob:
    print(-1)
    exit()
ans = len(X)+len(Y)
X.sort()
cnt = 0
lY = len(Y)
for i in range(len(X)):
    if lY == cnt:
        break
    if Y[cnt]<X[i]:
        ans-=1
        cnt+=1
    else:
        continue
print(ans)