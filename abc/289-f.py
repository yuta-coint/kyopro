sx,sy = map(int,input().split())
tx,ty = map(int,input().split())
a,b,c,d = map(int,input().split())
if (sx-tx)&1 or (sy-ty)&1:
    print("No")
    exit()
if b-a==0 and d-c==0:
    if sx==tx and ty==sy:
        print("Yes")
        exit()
    if a*2==sx+tx and c*2==sy+ty:
        print("Yes")
        print(a,c)
        exit()
    print("No")
    exit()
ansx = []
ansy = []
def checkx():
    key = (tx-sx)>>1
    if key>0:
        for i in range(key//(b-a)):
            ansx.append(a)
            ansx.append(b)
        ansx.append(a)
        ansx.append(a+(key%(b-a)))
    else:
        for i in range((-key)//(b-a)):
            ansx.append(b)
            ansx.append(a)
        ansx.append(b)
        ansx.append(b-((-key)%(b-a)))
def checky():
    key = (ty-sy)>>1
    if key>0:
        for i in range(key//(d-c)):
            ansy.append(c)
            ansy.append(d)
        ansy.append(c)
        ansy.append(c+(key%(d-c)))
    else:
        for i in range((-key)//(d-c)):
            ansy.append(d)
            ansy.append(c)
        ansy.append(d)
        ansy.append(d-((-key)%(d-c)))
if b==a:
    if sx==tx:
        checky()
    elif sx+tx==2*a:
        ansx.append(a)
        ansy.append(c)
        sy = 2*c-sy
        checky()
    else:
        print("No")
        exit()
elif c==d:
    if sy==ty:
        checkx()
    elif sy+ty==2*c:
        ansx.append(a)
        ansy.append(c)
        sx = 2*a-sx
        checkx()
    else:
        print("No")
        exit()
else:
    checkx()
    checky()
print("Yes")
lx = len(ansx)
ly = len(ansy)
if lx<ly:
    for i in range(ly-lx):
        ansx.append(a)
else:
    for i in range(lx-ly):
        ansy.append(c)
for i in range(max(lx,ly)):
    print(ansx[i],ansy[i])