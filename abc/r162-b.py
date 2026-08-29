N = int(input())
P = list(map(lambda x:int(x)-1,input().split()))
ans = []
goal = [i for i in range(N)]
def operate(i,j):
    cnt = 0
    newP = []
    for t in range(j):
        if cnt==i:
            cnt+=2
        newP.append(P[cnt])
        cnt+=1
    newP.append(P[i])
    newP.append(P[i+1])
    for t in range(j,N-2):
        if cnt==i:
            cnt+=2
        newP.append(P[cnt])
        cnt+=1
    ans.append((i+1,j))
    return newP
for i in range(N-2):
    k = P.index(goal[i])
    if k==i:
        continue
    if k==N-1:
        P = operate(N-2,N-3)
        k-=1
    P = operate(k,i)
if P==goal:
    print("Yes")
    l = len(ans)
    print(l)
    for t in range(l):
        print(ans[t][0],ans[t][1])
else:
    print("No")
