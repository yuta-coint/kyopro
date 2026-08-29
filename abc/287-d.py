S = input()
T = input()
lT = len(T)
#前は何文字までマッチするか
start = lT
for i in range(lT):
    if S[i]!="?" and T[i]!="?" and S[i]!=T[i]:
        start=i
        break
#後ろから何文字目まで
goal = lT
ls = len(S)
for i in range(lT):
    if S[ls-1-i]!="?" and T[lT-1-i]!="?" and S[ls-1-i]!=T[lT-1-i]:
        goal=i
        break
for i in range(lT+1):
    if i<=start and lT-i<=goal:
        print("Yes")
    else:
        print("No")