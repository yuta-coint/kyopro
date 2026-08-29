#端が崖になっているパターンは241-fで実装済み
def main():
    H,W,rs,cs = map(int,input().split())
    N = int(input())
    from bisect import bisect
    #r行目の様子をみる
    dr = {}
    wallr = [[0,W+1] for i in range(N)]
    dc = {}
    #c列目の様子をみる
    wallc = [[0,H+1] for i in range(N)]
    cnt1 = 0
    cnt2 = 0
    for i in range(N):
        r,c = map(int,input().split())
        if not (r in dr):
            dr[r]=cnt1
            cnt1+=1
        wallr[dr[r]].append(c)
        if not (c in dc):
            dc[c]=cnt2
            cnt2+=1
        wallc[dc[c]].append(r)
    for i in range(N):
        wallc[i].sort()
        wallr[i].sort()
    def U_instruction(l):
        if cs in dc:
            #print(wallc[dc[cs]])
            lim = wallc[dc[cs]][bisect(wallc[dc[cs]],rs)-1]
            #print(lim)
        else:
            lim = 0
        rs = max(rs-l,lim+1)
    def D_instruction(l):
        if cs in dc:
            lim = wallc[dc[cs]][bisect(wallc[dc[cs]],rs)]
        else:
            lim = H+1
        rs = min(rs+l,lim-1)
    def L_instruction(l):
        if rs in dr:
            lim = wallr[dr[rs]][bisect(wallr[dr[rs]],cs)-1]
        else:
            lim=0
        cs = max(cs-l,lim+1)
    def R_instruction(l):
        if rs in dr:
            lim = wallr[dr[rs]][bisect(wallr[dr[rs]],cs)]
        else:
            lim=W+1
        cs = min(cs+l,lim-1)
    Q=int(input())
    for i in range(Q):
        d,l = input().split()
        l = int(l)
        if d=="U":
            U_instruction(l)
        if d=="D":
            D_instruction(l)
        if d=="L":
            L_instruction(l)
        if d=="R":
            R_instruction(l)
        print(rs,cs)
main()