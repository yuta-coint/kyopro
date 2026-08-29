N = int(input())
R = list(input())
C= list(input())
for i in range(N):
    R[i] = ord(R[i])-ord("A")
    C[i] = ord(C[i])-ord("A")
#print(R,C)
from itertools import combinations,product
cand = list(combinations(range(N),3))
cand2 = []
for c in cand:
    cand2.append((c[0],c[2],c[1]))
cand+=cand2
lc = len(cand)
from copy import copy
for p1 in product(cand,repeat=2):
    c=[-1 for i in range(N)]
    for t in range(2):
        for i in range(3):
            if c[p1[t][i]]==-1:
                c[p1[t][i]]=(R[t]+i)%3
    flag = 0
    for i in range(N):
        if C[i]!=c[i] and c[i]!=-1:
            flag = 1
    if flag==1:
        continue
    for p2 in product(cand,repeat=N-2):
        c2 = copy(c)
        for t in range(N-2):
            for i in range(3):
                if c2[p2[t][i]]==-1:
                    c2[p2[t][i]]=(R[t+2]+i)%3
        flag = 0
        for i in range(N):
            if C[i]!=c2[i]:
                flag = 1
        if flag == 1:
            continue
            #print(p1,p2)
        ans = [['.' for y in range(N)] for x in range(N)]
        p3 = p1+p2
        for i in range(N):
            for j in range(3):
                ans[i][p3[i][j]] = chr(ord("A")+(R[i]+j)%3)
        for i in range(N):
            chka = True
            chkb = True
            chkc = True
            for j in range(N):
                if ans[j][i]=="A":
                    chka = False
                elif ans[j][i] == "B":
                    chkb = False
                elif ans[j][i] == "C":
                    chkc = False
            if chka or chkb or chkc:
                flag = 1
        if flag == 1:
            continue
        print("Yes")
        for i in range(N):
            print(*ans[i],sep="")
        exit()
print("No")




