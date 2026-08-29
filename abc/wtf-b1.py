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
    mid_r = N//2
    mid_l = (N-1)//2
    left  = []
    right = []
    final = []
    #最初に左右を操作するフェーズ
    if N&1:
        if mid_r-rP[mid_r]>0:
            pari = -1
        else:
            pari = 1
        for i in range(mid_r):
            if rP[i]<mid_r:
                s,t = i,rP[i]
                left.append((s,t))
                mani(s,t)
        for i in range(mid_r+1,N):
            if rP[i]>mid_r:
                s,t = i,rP[i]
                right.append((s,t))
                mani(s,t)
        #この段階で真ん中より左の小さいやつらとかはそろっている
        parent = mid_r
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
    elif rP[mid_l]>mid_l:
        for i in range(mid_r):
            if rP[i]<mid_r:
                s,t = i,rP[i]
                left.append((s,t))
                mani(s,t)
        for i in range(mid_r,N):
            if rP[i]>mid_l:
                s,t = i,rP[i]
                right.append((s,t))
                mani(s,t)
        parent = mid_l
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
        if rP[mid_r]<mid_r:
            pari = -1
        else:
            pari = 1
        for i in range(mid_l):
            if rP[i]<mid_r:
                s,t = i,rP[i]
                left.append((s,t))
                mani(s,t)
        for i in range(mid_r+1,N):
            if rP[i]>=mid_r:
                s,t = i,rP[i]
                right.append((s,t))
                mani(s,t)
        parent = mid_r
        if P[mid_l]==mid_l:
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
            elif P[parent]==rP[mid_l]:
                final.append((mid_l,parent))
                mani(parent,mid_l)
                final.append((mid_l,rP[mid_l]))
                mani(rP[mid_l],mid_l)
            elif P[parent]==rP[mid_r] and mid_r==parent:
                final.append((mid_r,rP[mid_r]))
                mani(rP[mid_r],mid_r)
            elif P[parent]==rP[mid_r]:
                final.append((mid_r,parent))
                mani(parent,mid_r)
                final.append((mid_r,rP[mid_r]))
                mani(rP[mid_r],mid_r)
            else:
                final.append((parent,P[parent]))
                mani(parent,P[parent])

    #print(left,right)
    print(len(left)+len(right)+len(final))
    if pari == 1:
        first = left
        second = right
    else:
        first=right
        second=left
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
    #print(P)