S = list(input())
K = int(input())
L = len(S)
for i in range(L):
    if S[i]!="o" and S[i]!="t":
        S[i]="t"
if S[L-1]=="o":
    S[L-1]="t"
for i in reversed(range(L-1)):
    if S[i]=="o" and S[i+1]=="t":
        S[i]="t"
#K個消せるなら全部消す。
#oとfの間は消しきれる状態でなければならない。適当にfを間引いていく