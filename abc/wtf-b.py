import copy
def mani(s,t):
    rP[P[s]],rP[P[t]]=t,s
    P[s],P[t]=P[t],P[s]
def ap(s,t):
    if s>t:
        s,t = t,s
    ans.append((s+1,t+1))
    print(s+1,t+1)
def judge(ans):
    if len(ans)>=N:
        print(P0)
        return False
    if ideal!=P:
        print(P0)
        return False
    for i in range(len(ans)-1):
        l,r = ans[i]
        ll,rr = ans[i+1]
        if l>=rr or r<=ll:
            continue
        print(P0)
        return False
    return True

T  =int(input())
for case in range(T):
    flag = 0
    N = int(input())
    P = list(map(lambda x:int(x)-1,input().split()))
    P0=copy(P)
    rP = {}
    for i in range(N):
        rP[P[i]]=i
    mid = N//2
    ml = max(0,mid-1)
    left  = []
    right = []
    final = []
    #最初に左右を操作するフェーズこ
    if N&1:
        if mid-rP[mid]>0:
            pari = -1
        else:
            pari = 1
        for i in range(mid):
            if rP[i]<mid:
                s,t = i,rP[i]
                left.append((s,t))
                mani(s,t)
        for i in range(mid+1,N):
            if rP[i]>mid:
                s,t = i,rP[i]
                right.append((s,t))
                mani(s,t)
    #この段階で真ん中より左の小さいやつらとかはそろっている
        parent = mid
        for i in range(N-len(left)-len(right)):
            if P[parent]==parent:
                while P[parent]==parent:
                    parent+=1
                    if parent==N:
                        break
                if parent==N:
                    break
                final.append((0,0))
            else:
                s,t = parent,P[parent]
                final.append((s,t))
                mani(s,t)
    elif rP[ml]>ml:
        flag =1
        for i in range(mid):
            if rP[i]<mid:
                s,t = i,rP[i]
                left.append((s,t))
                mani(s,t)
        for i in range(mid,N):
            if rP[i]>=mid:
                s,t = i,rP[i]
                right.append((s,t))
                mani(s,t)
        parent = ml
        pari = -1
        for i in range(N-len(left)-len(right)):
            if P[parent]==parent:
                while P[parent]==parent:
                    parent-=1
                    if parent==-1:
                        break
                if parent==-1:
                    break
                final.append((0,0))
            else:
                final.append((parent,P[parent]))
                mani(parent,P[parent])
    else:
        flag = 2
        if rP[mid]<mid:
            pari = -1
        else:
            pari = 1
        for i in range(ml):
            if rP[i]<mid:
                s,t = i,rP[i]
                left.append((s,t))
                mani(s,t)
        for i in range(mid+1,N):
            if rP[i]>=mid:
                s,t = i,rP[i]
                right.append((s,t))
                mani(s,t)
        parent = mid
        if P[ml]==ml:
            final.append((0,0))
            mani(0,0)
        for i in range(N-len(left)-len(right)):
            if parent==N:
                break
            if P[parent]==parent:
                while P[parent]==parent:
                    parent+=1
                    if parent==N:
                        break
                if parent==N:
                    break
                final.append((0,0))
            elif P[parent]==rP[ml]:
                final.append((ml,parent))
                mani(parent,ml)
                final.append((ml,rP[ml]))
                mani(rP[ml],ml)
            elif P[parent]==rP[mid] and mid==parent:
                final.append((mid,rP[mid]))
                mani(rP[mid],mid)
            elif P[parent]==rP[mid]:
                final.append((mid,parent))
                mani(parent,mid)
                final.append((mid,rP[mid]))
                mani(rP[mid],mid)
            else:
                final.append((parent,P[parent]))
                mani(parent,P[parent])

    #print(left,right)  
    print(len(left)+len(right)+len(final))
    if pari == 1:
        first = copy(left)
        second = copy(right)
    else:
        first=copy(right)
        second=copy(left)
    assert 0<=len(first)-len(second)<=1
    ans = []
    for i in range(len(second)):
        s,t = first[i]
        ap(s,t)
        s,t = second[i]
        ap(s,t)
    if len(first)>len(second):
        s,t = first[-1]
        ap(s,t)
    for s,t in final:
        ap(s,t)
    ideal = [i for i in range(N)]
    if flag == 2:
        assert judge(ans)
    #print(P)