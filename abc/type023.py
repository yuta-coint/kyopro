H,W  = map(int,input().split())
mod = 10**9+7
import sys
sys.setrecursionlimit(10**7)
C = [list(input()) for i in range(H)]
#キングがいるか否か
valid = []
def vl(left,i,odd):
    if i==W:
        valid.append(left)
        return(0)
    if odd==1:
        vl(left*2,i+1,0)
    else:
        vl(left*2+1,i+1,1)
        vl(left*2,i+1,0)
vl(0,0,0)
#print(valid)
#その状況数える必要がありますか？
l_valid = len(valid)
#前wマスの状態
d_valid = {valid[i]:i for i in range(l_valid)}
ans_king = [0 for i in range(l_valid)]
ans_no_king = []
#一行目が行けるかどうかを調べていくんだけど
black = 0
for j in range(W):
    if C[0][j]=="#":
        black+=1<<j
for situation in valid:
    if situation&black>0:
        ans_no_king.append(0)
    else:
        ans_no_king.append(1)
#print(ans_king,ans_no_king)
for i in range(1,H):
    new_king = []
    new_no_king = []
    #左端の例外処理。列が新しくなるのでW+1個前を考える必要がない
    for situation in valid:
        if situation & 1:
            if C[i][0]=="." and (situation-1) in d_valid:
                new_no_king.append((ans_king[d_valid[situation-1]]+ans_no_king[d_valid[situation-1]])%mod)
            else:
                new_no_king.append(0)
            new_king.append(0)
        else:
            if (situation+1) in d_valid:
                new_no_king.append((ans_king[d_valid[situation]]+ans_no_king[d_valid[situation]])%mod)
                new_king.append((ans_king[d_valid[situation+1]]+ans_no_king[d_valid[situation+1]])%mod)
            else:
                new_no_king.append((ans_king[d_valid[situation]]+ans_no_king[d_valid[situation]])%mod)
                new_king.append(0)
    ans_king = new_king
    ans_no_king = new_no_king
    #print(ans_king,ans_no_king)
    for j in range(1,W):
        #左端は例外処理が必要…
        #上にkingがある
        new_king = []
        new_no_king = []
        for situation in valid:
            if (situation>>j)&1:
                if C[i][j]=="#":
                    new_no_king.append(0)
                else:
                    if situation-(1<<j) in d_valid:
                        new_no_king.append(ans_no_king[d_valid[situation-(1<<j)]])
                    else:
                        new_no_king.append(0)
                new_king.append(0)
            else:
                new_no_king.append((ans_no_king[d_valid[situation]]+ans_king[d_valid[situation]])%mod)
                if situation+(1<<j) in d_valid:
                    new_king.append(ans_no_king[d_valid[situation+(1<<j)]])
                else:
                    new_king.append(0)
        ans_king = new_king
        ans_no_king = new_no_king
        #print(ans_king,ans_no_king)
print((sum(ans_king)+sum(ans_no_king))%mod)