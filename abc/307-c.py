Ha,Wa = map(int,input().split())
A = [input() for i in range(Ha)]
Hb,Wb = map(int,input().split())
B= [input() for i in range(Hb)]
Hx,Wx = map(int,input().split())
X= [input() for i in range(Hx)]
part = 0
for i in range(Ha):
    part+=A[i].count("#")
for i in range(Hb):
    part+=B[i].count("#")
x_cnt = 0
for i in range(Hx):
    x_cnt+=X[i].count("#")
if part<x_cnt:
    print("No")
    exit()
rem = part-x_cnt
for ait in range(20):
    for ajt in range(20):
        for bit in range(20):
            for bjt in range(20):
                ai,aj,bi,bj = ait-10,ajt-10,bit-10,bjt-10
                flag =0
                over = 0
                for xi in range(Hx):
                    for xj in range(Wx):
                        temp = "."
                        o = 0
                        if 0<=xi+ai<Ha and 0<=xj+aj<Wa:
                            if A[xi+ai][xj+aj]=="#":
                                temp = "#"
                                o+=1
                        if 0<=xi+bi<Hb and 0<=xj+bj<Wb:
                            if B[xi+bi][xj+bj]=="#":
                                temp = "#"
                                o+=1
                        if o==2:
                            over+=1
                        if X[xi][xj]!=temp:
                            flag =1
                            break
                    if flag==1:
                        break
                else:
                    if over==rem:
                        print("Yes")
                        exit()
print("No")