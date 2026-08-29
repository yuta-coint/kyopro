N,X,Y = map(int,input().split())
A = list(map(int,input().split()))
vert = [A[i] for i in range(0,N,2)]
para = [A[i] for i in range(1,N,2)]
sY = Y+sum(vert)
sX = X+sum(para)
if sX&1 or sY&1:
    print("No")
    exit()
sX//=2
sY//=2
#いくつか取り出して和を所望のやつにする
def half_Knap(P,S):
    lP = len(P)
    cut = lP//2
    all_score= []
    for bits in range(1<<cut):
        score = 0
        for i in range(cut):
            if (bits>>i)&1:
                score+=P[i]
        all_score.append(score)
    s_score = set(all_score)
    for bits in range(1<<(lP-cut)):
        score = 0
        for i in range(lP-cut):
            if (bits>>i)&1:
                score+=P[i+cut]
        if score>S:
            continue
        if (S-score) in s_score:
            return (all_score.index(S-score)+bits*(1<<cut))
    return -1
ansX = half_Knap(para,sX)
ansY = half_Knap(vert,sY)
if ansX==-1 or ansY==-1:
    print("No")
    exit()
side = [0 for i in range(N+1)]
for i in range(0,N,2):
    if (ansY>>(i//2))&1:
        side[i+1]=1
    else:
        side[i+1]=3
for i in range(1,N,2):
    if (ansX>>(i//2))&1:
        side[i+1]=0
    else:
        side[i+1]=2
ans = []
for i in range(N):
    if (side[i+1]-side[i])%4==1:
        ans.append("L")
    else:
        ans.append("R")
print("Yes")
print(*ans,sep = "")
