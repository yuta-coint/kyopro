N,M = map(int,input().split())
tate = set()
yoko = set()
wa = set()
sa = set()
for i in range(M):
    a,b = map(int,input().split())
    tate.add(a)
    yoko.add(b)
    wa.add(a+b)
    sa.add(a-b)
first = 0
for i in tate:
    first+=N
for j in yoko:
    first+=N
for i in wa:
    first += N-abs(N+1-i)
for i in sa:
    first += N-abs(i)
#一回登場する奴は一回、三回登場する奴は2回、六回登場する奴は3回引く
from collections import defaultdict
kaburi = defaultdict(int)
chk = set()
for i in tate:
    for j in yoko:
        kaburi[(i)*10**10+(j)]+=1
        chk.add((i)*10**10+(j))
for i in wa:
    for j in sa:
        if (i-j)&1:
            continue
        if 1<=(i+j)//2<=N and 1<=(i-j)//2<=N:
            kaburi[((i+j)//2)*10**10+((i-j)//2)]+=1
            chk.add(((i+j)//2)*10**10+((i-j)//2))
for i in tate:
    for j in wa:
        if 1<=j-i<=N:
            kaburi[(i)*10**10+(j-i)]+=1
            chk.add((i)*10**10+(j-i))
for i in tate:
    for j in sa:
        if 1<=i-j<=N:
            kaburi[(i)*10**10+(i-j)]+=1
            chk.add((i)*10**10+(i-j))
for i in yoko:
    for j in wa:
        if 1<=j-i<=N:
            kaburi[(j-i)*10**10+(i)]+=1
            chk.add((j-i)*10**10+(i))
for i in yoko:
    for j in sa:
        if 1<=i+j<=N:
            kaburi[(i+j)*10**10+(i)]+=1
            chk.add((i+j)*10**10+(i))
#print(first)
second = 0
print(kaburi)
for k in chk:
    if kaburi[k]==1:
        second-=1
    elif kaburi[k]==3:
        second-=2
    elif kaburi[k]==6:
        second-=3
print(N*N-first-second)