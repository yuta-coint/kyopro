N,L,R = map(int,input().split())
import sys
ssf = sys.stdout.flush
def my_turn():
    #各成分の長さと右端を格納する
    elements = []
    #とりあえず計算する
    cnt = 0
    G_now=0
    for i in range(1,N+1):
        if exists[i]:
            cnt+=1
        else:
            if cnt>0:
                elements.append((cnt,i-1))
                G_now^=Grundy[cnt]
                cnt=0
    if cnt>0:
        elements.append((cnt,N))
        G_now^=Grundy[cnt]
    for s,t in elements:
        if s<L:
            continue
        for i in range(s-L+1):
            if Grundy[i]^Grundy[s-L-i]^Grundy[s]^G_now==0:
                print(t-s+1+i,L)
                ssf()
                for j in range(t-s+1+i,t-s+1+i+L):
                    exists[j]=False
                return()
    print(0,0)

#L=Rが意外と難儀
if L<R:
    print("First")
    ssf()
    if N&1 and L&1:
        print((N-L+2)//2,L)
    elif N&1:
        print((N-L+1)//2,L+1)
    elif L&1:
        print((N-L+1)//2,L+1)
    else:
        print((N-L+2)//2,L)
    ssf()
    while True:
        a,b = map(int,input().split())
        if (a,b) ==(0,0) or (a,b)==(-1,-1):
            exit()
        print(N+2-a-b,b)
        ssf()
else:
    #L枚未満なら負けてる
    Grundy = [0 for i in range(N+2)]
    for num_cards in range(L,N+2):
        #次に入れない所で一番小さいやつ
        next = [False for _ in range(N+2)]
        for x in range(num_cards-L+1):
            next[Grundy[x]^Grundy[num_cards-x-L]]=True
        for j in range(N+2):
            if next[j]==False:
                Grundy[num_cards]=j
                break
    #print(Grundy)
    exists = [True for i in range(N+1)]
    if Grundy[N]==0:
        print("Second")
        ssf()
    else:
        print("First")
        ssf()
        my_turn()
    while True:
        a,b = map(int,input().split())
        if (a,b) ==(0,0) or (a,b)==(-1,-1):
            exit()
        for i in range(a,a+b):
            exists[i] = False
        my_turn()