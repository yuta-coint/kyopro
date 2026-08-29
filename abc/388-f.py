from copy import copy
#A=1なら目の前のマスにひたすら飛んでいけば良いだけだが…
N,M,A,B = map(int,input().split())
#間に悪いマスが無ければ何マス飛びができるか？(400マスあれば飛べる)
reachable = [False for i in range(400)]
reachable[0] = True
for i in range(A,B+1):
    reachable[i]=True
for i in range(B+1,400):
    for j in range(A,B+1):
        if reachable[i-j]==True:
            reachable[i] = True
            break
#悪いマスの長さ+その前のマスで計Bマスについて到達可能かを判定したい
#R-(B-1)番から調べていきたい
#chk:R-B-1
#R+1からR+Bまでの様子。
head = []
for i in range(M):
    L,R = map(int,input().split())
    if (R-L+1)>=B:
        print("No")
        exit()
    if i==0:
        tale = [False for j in range(B)]
        for j in range(B):
            if R-(B-1)+j>=L:
                continue
            if R-(B-1)+j-1>=400:
                tale[j] = True
                continue
            tale[j] = reachable[R-(B-1)+j-1]
    else:
        ptale = copy(tale)
        tale = []
        for j in range(B):
            cur = R-(B-1)+j
            if pR-B+1<=cur<=pR:
                tale.append(ptale[cur-(pR-B+1)])
                continue
            if pR+1<=cur<=pR+B:
                tale.append(head[cur-(pR+1)])
                continue
            tale.append(False)
            for past in range(pR+1,pR+B+1):
                if head[past-(pR+1)]:
                    if cur-past>=400:
                        tale[-1] = True
                    if 0<=cur-past<400:
                        if reachable[cur-past]:
                            tale[-1]=True
        for j in range(B-(R-L+1),B):
            tale[j]=False
    head = [False for j in range(B)]
    for ima in range(B):
        for deme in range(A,B+1):
            if ima-deme>=0:
                if head[ima-deme]:
                    head[ima] = True
            else:
                if tale[ima+B-deme]:
                    head[ima] = True
    pR = R
    #print(tale)
    #print(head)
ans = False
if R-B+1<=N<=R:
    ans = tale[cur-(R-B+1)]
elif R+1<=N<=R+B:
    ans = head[cur-(R+1)]
else:
    for past in range(R+1,R+B+1):
        if head[past-(R+1)]:
            if N-past>=400:
                ans = True
            elif 0<=N-past<400:
                if reachable[N-past]:
                    ans = True
if ans:
    print("Yes")
else:
    print("No")

fac = [1]
for i in range(1,N):
    fac.append(fac[-1]*i)