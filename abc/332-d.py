H,W = map(int,input().split())
A = [list(map(int,input().split())) for i in range(H)]
B = [list(map(int,input().split())) for i in range(H)]
from itertools import permutations
ans = 10**9
def change(seq,L):
    temp = [seq[i] for i in range(L)]
    cnt = 0
    while True:
        flag = True
        for i in range(L-1):
            if temp[i]>temp[i+1]:
                cnt+=1
                flag=False
                temp[i],temp[i+1] = temp[i+1],temp[i]
        if flag:
            break
    return(cnt)
        
for s1 in permutations(range(H),H):
    changeH = change(s1,H)
    for s2 in permutations(range(W),W):
        newA = [[] for i in range(H)]
        for x in range(H):
            for y in range(W):
                newA[x].append(A[s1[x]][s2[y]])
        if newA==B:
            changeW  = change(s2,W)
            if changeH+changeW<ans:
                ans = changeH+changeW
if ans == 10**9:
    print(-1)
else:
    print(ans)