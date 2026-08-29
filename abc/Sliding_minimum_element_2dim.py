from collections import deque
#H,W,L　H×Lのリストの中からL*Dの最小値を求める
#H,W,L,Dはそれぞれの箱の大きさ
H,W,L,D = map(int,input().split())
a = [list(map(int,input().split())) for i in range(H)]
column = [deque([]) for i in range(W)]
for j in range(H):
    nex = []
    window = deque([])
    r = (a[j][0],0)
    ans = []
    #各列にその行の情報を突っ込む
    for i in range(W):
        f = 0
        if window:
            r=window.pop()
            f = 1
        while r[0]>a[j][i] and window:
            r=window.pop()
        if (r[0]<=a[j][i] or i==0) and f==1:
            window.append(r)
        window.append((a[j][i],i))
        if i<L-1:
            continue
        l = window.popleft()
        nex.append(l[0])
        if l[1]>i+1-L:
            window.appendleft(l)
    #各columnに対して一手分の処理をする
    for i in range(W):
        f = 0
        if column[i]:
            r=column[i].pop()
            f = 1
        while r[0]>nex[i] and column[i]:
            r=column[i].pop()
        if (r[0]<=nex[i] or i==0) and f==1:
            column[i].append(r)
        column[i].append((nex[i],i))
        if j<D-1:
            continue
        l = column[i].popleft()
        column[i].append(l[0])
        if l[1]>j+1-D:
            column[i].appendleft(l)
print(*ans)