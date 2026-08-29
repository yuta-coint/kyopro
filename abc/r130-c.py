import copy
a= input()
b =input()
change = False
if len(a)<len(b):
    a,b = b,a
    change = True
counta = [0 for i in range(10)]
countb = [0 for i in range(10)]
for i in range(len(a)):
    counta[int(a[i])]+=1
for i in range(len(b)):
    countb[int(b[i])]+=1
ansa = [[int(a[i]) for i in range(len(a))]]
ansb = [[int(b[i]) for i in range(len(b))]]
for a1 in range(10):
    ca = copy.copy(counta)
    cb = copy.copy(countb)
    if ca[a1]==0:
        continue
    ca[a1]-=1
    aa = []
    ab = []
    for i in range(10-a1,10):
        if cb[i]>0:
            cb[i]-=1
            b1 = i
            break
    else:
        continue
    for i in range(1,9):
        for j in range(9-i,10):
            m = min(ca[i],cb[j])
            for _ in range(m):
                aa.append(i)
                ab.append(j)
            ca[i]-=m
            cb[j]-=m
    aa1 = []
    ab1 = []
    for i in reversed(range(10)):
        for _ in range(ca[i]):
            aa1.append(i)
        for _ in range(cb[i]):
            ab1.append(i)
    ansa.append([a1]+aa+aa1)
    ansb.append([b1]+ab+ab1)
kurimax = 0
ansn = 0
for i in range(len(ansa)):
    kuri = 0
    for j in range(len(b)):
        if ansa[i][j]+ansb[i][j]>=9:
            kuri+=1
        else:
            break
    for j in range(len(b),len(a)):
        if ansa[i][j]==9:
            kuri+=1
        else:
            break
    if kuri>=kurimax:
        ansn=i
        kurimax=kuri
if change == True:
    ansa[ansn],ansb[ansn]=ansb[ansn],ansa[ansn]
ans = [ansa[ansn][i] for i in reversed(range(len(ansa[ansn])))]
print(*ans,sep="")
ans = [ansb[ansn][i] for i in reversed(range(len(ansb[ansn])))]
print(*ans,sep="")