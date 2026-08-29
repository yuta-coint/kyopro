P1 = [list(input()) for i in range(4)]
P2 = [list(input()) for i in range(4)]
P3 = [list(input()) for i in range(4)]
white = ["." for i in range(4)]
from copy import deepcopy
def para(PP):
    #可能な限り左上に寄せる
    P = deepcopy(PP)
    flag = 0
    while True:
        for j in range(4):
            if P[0][j]=="#":
                flag = 1
        if flag == 1:
            break
        for i in range(4):
            for j in range(4):
                if i<3:
                    P[i][j] = P[i+1][j]
                else:
                    P[i][j] = "."
    while True:
        flag = 0
        for i in range(4):
            if P[i][0]=="#":
                flag = 1
        if flag == 1:
            break 
        for i in range(4):
            for j in range(4):
                if j<3:
                    P[i][j] = P[i][j+1]
                else:
                    P[i][j] = "."
    #下に何段階で寄せられる？
    bot = 4
    right = 4
    for i in range(4):
        for j in range(4):
            if P[i][j]=="#":
                bot = min(bot,4-i)
                right = min(right,4-j)
    re = []
    for x in range(bot):
        for y in range(right):
            Q = [["." for j in range(4)] for i in range(4)]
            for i in range(4):
                for j in range(4):
                    if i+x<4 and j+y<4:
                        Q[i+x][j+y] = P[i][j]
            re.append(Q)
    return re
def cyc(P):
    Q = [["." for j in range(4)] for i in range(4)]
    for i in range(4):
        for j in range(4):
            Q[j][3-i] = P[i][j]
    return Q
def listup(PPP):
    r = []
    for _ in range(4):
        for rr in para(PPP):
            r.append(rr)
        PPP = cyc(PPP)
    return r
L1 = listup(P1)
L2 = listup(P2)
L3 = listup(P3)
for r1 in L1:
    for r2 in L2:
        for r3 in L3:
            flag = 0
            for i in range(4):
                for j in range(4):
                    cnt = 0
                    if r1[i][j]=="#":
                        cnt+=1
                    if r2[i][j]=="#":
                        cnt+=1
                    if r3[i][j]=="#":
                        cnt+=1
                    if cnt!=1:
                        flag = 1
                        break
                if flag==1:
                    break
            if flag==0:
                print("Yes")
                exit()
print("No")