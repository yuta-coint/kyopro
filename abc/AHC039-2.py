def ruiseki(tab,h,w):
    temp_sum = [[0 for j in range(w+1)] for i in range(h+1)]
    for i in range(h):
        for j in range(w):
            temp_sum[i+1][j+1] = temp_sum[i][j+1]+temp_sum[i+1][j]-temp_sum[i][j]+tab[i][j]
    s,t = 1,1
    for i in range(1,h+1):
        for j in range(1,w+1):
            if temp_sum[i][j]>=temp_sum[s][t]:
                s,t = i,j
    return s,t
N = int(input())
M = 10**5
haba = 100
masu = M//haba
sea = [[0 for i in range(M//haba)] for j in range(M//haba)]
for i in range(N):
    x,y = map(int,input().split())
    if x==10**5:
      x-=1
    else:
      y-=1
    sea[x//haba][y//haba]+=1
for i in range(N):
    x,y = map(int,input().split())
    if x==10**5:
      x-=1
    else:
      y-=1
    sea[x//haba][y//haba]-=1
LD = [[-sea[i][j] for j in range(masu//2)] for i in range(masu//2)]
LU = [[-sea[i][masu-1-j] for j in range(masu//2-1)] for i in range(masu//2)]
RD = [[-sea[masu-1-i][j] for j in range(masu//2)] for i in range(masu//2-1)]
RU = [[-sea[masu-1-i][masu-1-j] for j in range(masu//2-1)] for i in range(masu//2-1)]
p1,q1 = ruiseki(LD,masu//2,masu//2)
p2,q2 = ruiseki(LU,masu//2,masu//2-1)
p3,q3 = ruiseki(RU,masu//2-1,masu//2-1)
p4,q4= ruiseki(RD,masu//2-1,masu//2)
temp_min = 0
ind1 = 0
cnt = 0
for j in range(min(q1,q4)-1):
    for i in range(p1,masu-p4):
        cnt+=sea[i][j]
    if temp_min>=cnt:
        temp_min = cnt
        ind1 = j+1
temp_min = 0
ind2 = 0
cnt = 0
for i in range(min(p1,p2)-1):
    for j in range(q1,masu-q2):
        cnt+=sea[i][j]
    if temp_min>=cnt:
        temp_min = cnt
        ind2 = i+1
temp_min = 0
ind3 = masu
cnt = 0
for j in reversed(range(masu-min(q2,q3)+1,masu)):
    for i in range(p2,masu-p3):
        cnt+=sea[i][j]
    if temp_min>=cnt:
        temp_min = cnt
        ind3 = j
temp_min = 0
ind4 = masu
cnt = 0
for i in reversed(range(masu-min(p3,p4)+1,masu)):
    for j in range(q4,masu-q3):
        cnt+=sea[i][j]
    if temp_min>=cnt:
        temp_min = cnt
        ind4 = i
part1,part2,part3,part4 = [(p1,ind1),(p1,q1),(ind2,q1)],[(ind2,masu-q2),(p2,masu-q2),(p2,ind3)],[(masu-p3,ind3),(masu-p3,masu-q3),(ind4,masu-q3)],[(ind4,q4),(masu-p4,q4),(masu-p4,ind1)]
out = [(p1,ind1),(p1,q1),(ind2,q1),(ind2,masu-q2),(p2,masu-q2),(p2,ind3),(masu-p3,ind3),(masu-p3,masu-q3),(ind4,masu-q3),(ind4,q4),(masu-p4,q4),(masu-p4,ind1)]
#print(12)
#for p,q in out:
#    print(p*haba,q*haba)
if q4-ind1>2 and ind4-(masu-p4)>2:
    RD = [[sea[ind4-i][q4-j] for j in range(q4-ind1-1)] for i in range(ind4-(masu-p4)-1)]
    r4,s4 = ruiseki(RD,ind4-(masu-p4)-1,q4-ind1-1)
    part4 = [(ind4,q4-s4),(ind4-r4,q4-s4),(ind4-r4,q4),(masu-p4,q4),(masu-p4,ind1)]
if p1-ind2>2 and q1-ind1>2:
    LD = [[sea[p1-i][ind1+j] for j in range(q1-ind1-1)] for i in range(p1-ind2-1)]
    r1,s1 = ruiseki(LD,p1-ind2-1,q1-ind1-1)
    part1 = [(p1-r1,ind1),(p1-r1,ind1+s1),(p1,ind1+s1),(p1,q1),(ind2,q1)]
q2 = masu-q2
if p2-ind2>2 and ind3-q2>2:
    LU = [[sea[ind2+i][q2+j] for j in range(ind3-q2-1)] for i in range(p2-ind2-1)]
    r2,s2 = ruiseki(LU,p2-ind2-1,ind3-q2-1)
    part2 = [(ind2,q2+s2),(ind2+r2,q2+s2),(ind2+r2,q2),(p2,q2),(p2,ind3)]
q3 = masu-q3
p3 = masu-p3
out = part1+part2+part3+part4
print(len(out))
for p,q in out:
    print(p*haba,q*haba)
