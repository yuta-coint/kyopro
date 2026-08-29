def main():
    N,x,y = map(int,input().split())
    armx = []
    army = []
    A = list(map(int,input().split()))
    for i in range(1,N):
        if i&1:
            army.append(A[i])
        else:
            armx.append(A[i])
    x-=A[0]
    x+=sum(armx)
    y+=sum(army)
    if x&1 or y&1 or x<0 or y<0:
        print("No")
    else:
        x>>=1
        y>>=1
        dpx = [False for i in range(x+1)]
        dpy = [False for i in range(y+1)]
        dpx[0]=True
        dpy[0]=True
        for t in armx:
            if t>x:
                continue
            for i in reversed(range(t,x+1)):
                if dpx[i-t]:
                    dpx[i]=True
        for t in army:
            if t>y:
                continue
            for i in reversed(range(t,y+1)):
                if dpy[i-t]:
                    dpy[i]=True
        if dpx[x] and dpy[y]:
            print("Yes")
        else:
            print("No")
main()