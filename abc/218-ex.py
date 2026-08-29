#https://sapphire15.hatenablog.com/entry/2022/05/30/012835
N,R = map(int,input().split())
A = list(map(int,input().split()))
if 2*R>N:
    R = N-R
def Alien(c):
    #ここでmin(f(x)-cx)を高速に計算する。さらに、minとなるようなxも調べる
    #本問の場合、「1つ赤にするたびにCのボーナス」で「ついていないランプ」の最小値を求める。
    scorer,scoreb = -c,0
    mar,mab = 1,0
    mir,mib = 1,0
    for i in range(N-1):
        if scorer-c+A[i]<scoreb-c:
            new_mar = mar+1
            new_mir = mir+1
        elif scorer-c+A[i]==scoreb-c:
            new_mar = max(mar,mab)+1
            new_mir = min(mir,mib)+1
        else:
            new_mar = mab+1
            new_mir = mib+1
        if scorer<scoreb+A[i]:
            new_mab = mar
            new_mib = mir
        elif scorer==scoreb+A[i]:
            new_mab = max(mar,mab)
            new_mib = min(mir,mib)
        else:
            new_mab = mab
            new_mib = mib
        scorer,scoreb = min(scorer-c+A[i],scoreb-c),min(scorer,scoreb+A[i])
        mar,mir,mab,mib=new_mar,new_mir,new_mab,new_mib
    if scorer<scoreb:
        return (scorer,mir,mar)
    else:
        return (scoreb,mib,mab)
#Alienのlog倍でf(k)を計算できる。
def dp(k):
    m = -10**14+1
    M = 10**14+1
    while True:
        temp = (M+m)//2
        sc,indmi,indma  = Alien(temp)
        #print(temp,sc,ind)
        if indmi>k:
            M = temp
        elif indmi<=k<=indma:
            break
        else:
            m  =temp
    #sc,indmi,indma  = Alien(temp)
    return temp*k+sc
#実数でdpするならこっち！##########################
def dp(k):
    m = -10**14+1
    M = 10**14+1
    while (M-m)>10**(-9):
        temp = (M+m)/2
        sc,indmi  = Alien(temp)
        #print(temp,sc,ind)
        if indmi>k:
            M = temp
        else:
            m  =temp
    #sc,indmi,indma  = Alien(temp)
    return temp*k+sc
from math import floor
print(sum(A)-floor(dp(R)+0.5))
