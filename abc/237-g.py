import sys
input = sys.stdin.readline

N,Q,x=map(int,input().split())
N+=1
seg_el=1<<(N.bit_length()) # Segment treeの台の要素数
seg_height=1+N.bit_length() # Segment treeの高さ
SEG=[0]*(2*seg_el) # 1-indexedなので、要素数2*seg_el.Segment treeの初期値で初期化
LAZY=[None]*(2*seg_el) # 1-indexedなので、要素数2*seg_el.Segment treeの初期値で初期化

def indexes(L,R): # 遅延伝搬すべきノードのリストを返す. （つまり, updateやgetvaluesで見るノードより上にあるノードたち）
    INDLIST=[]

    R-=1
    
    L>>=1
    R>>=1

    while L!=R:
        if L>R:
            INDLIST.append(L)
            L>>=1
        else:
            INDLIST.append(R)
            R>>=1

    while L!=0:
        INDLIST.append(L)
        L>>=1

    return INDLIST

def updates(l,r,x): # 区間[l,r)をxに更新
        
    L=l+seg_el
    R=r+seg_el

    L//=(L & (-L))
    R//=(R & (-R))

    UPIND=indexes(L,R)
    
    for ind in UPIND[::-1]: # 遅延伝搬
        if LAZY[ind]!=None:
            update_lazy = LAZY[ind] *(1<<(seg_height - 1 - (ind.bit_length())))
            LAZY[ind<<1]=LAZY[1+(ind<<1)]=LAZY[ind]
            SEG[ind<<1]=SEG[1+(ind<<1)]=update_lazy
            LAZY[ind]=None

    while L!=R:
        if L > R:
            SEG[L]=x * (1<<(seg_height - (L.bit_length())))
            LAZY[L]=x
            L+=1
            L//=(L & (-L))

        else:
            R-=1
            SEG[R]=x * (1<<(seg_height - (R.bit_length())))
            LAZY[R]=x
            R//=(R & (-R))

    for ind in UPIND:
        SEG[ind]=SEG[ind<<1]+SEG[1+(ind<<1)]

def getvalues(l,r): # 区間[l,r)に関するminを調べる

    L=l+seg_el
    R=r+seg_el

    L//=(L & (-L))
    R//=(R & (-R))

    UPIND=indexes(L,R)
    
    for ind in UPIND[::-1]: # 遅延伝搬
        if LAZY[ind]!=None:
            update_lazy = LAZY[ind] *(1<<(seg_height - 1 - (ind.bit_length())))
            LAZY[ind<<1]=LAZY[1+(ind<<1)]=LAZY[ind]
            SEG[ind<<1]=SEG[1+(ind<<1)]=update_lazy
            LAZY[ind]=None
            
    ANS=0

    while L!=R:
        if L > R:
            ANS+=SEG[L]
            L+=1
            L//=(L & (-L))

        else:
            R-=1
            ANS+=SEG[R]
            R//=(R & (-R))

    return ANS



import sys
input = sys.stdin.readline
x_position = -1
P = list(map(int,input().split()))
for i in range(N-1):
    if P[i]==x:
        x_position=i+1
    elif P[i]>x:
        updates(i+1,i+2,1)
for _ in range(Q):
    c,l,r = map(int,input().split())
    one_count = getvalues(l,r+1)
    #print(one_count)
    if c==1:
        updates(r+1-one_count,r+1,1)
        updates(l,r+1-one_count,0)
        if l<=x_position<=r:
            x_position = r-one_count
    else:
        updates(l+one_count,r+1,0)
        updates(l,l+one_count,1)
        if l<=x_position<=r:
            x_position = l+one_count
print(x_position)

