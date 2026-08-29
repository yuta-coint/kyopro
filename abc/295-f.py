T = int(input())
def cal(X,S):
    LS = len(S)
    ans = 0
    if S[0]!="0":
        SS = int(S)
        for i in range(16):
            #print(ans)
            cand1  = X-X%(10**(i+LS))+((SS+1)*(10**i))-1
            if cand1<=X:
                ans+=1+(cand1//(10**(i+LS)))*(10**i)+cand1%(10**i)
                continue
            if (X%(10**(i+LS)))//(10**i)==SS:
                cand1 = X
                ans+=1+(cand1//(10**(i+LS)))*(10**i)+cand1%(10**i)
                continue
            cand1 -= 10**(i+LS)
            if cand1<=X:
                ans+=1+(cand1//(10**(i+LS)))*(10**i)+cand1%(10**i)
                continue
    else:
        SS = int(S)
        for i in range(16):
            #print(ans)
            cand1  = X-X%(10**(i+LS))+((SS+1)*(10**i))-1
            if cand1<=X:
                if 1+(cand1//(10**(i+LS)))*(10**i)+cand1%(10**i)-10**i>0:
                    ans+=1+(cand1//(10**(i+LS)))*(10**i)+cand1%(10**i)-10**i
                continue
            if (X%(10**(i+LS)))//(10**i)==SS:
                cand1 = X
                if 1+(cand1//(10**(i+LS)))*(10**i)+cand1%(10**i)-10**i>0:
                    ans+=1+(cand1//(10**(i+LS)))*(10**i)+cand1%(10**i)-10**i
                continue
            cand1 -= 10**(i+LS)
            if cand1<=X:
                if 1+(cand1//(10**(i+LS)))*(10**i)+cand1%(10**i)-10**i>0:
                    ans+=1+(cand1//(10**(i+LS)))*(10**i)+cand1%(10**i)-10**i
                continue
    #print(ans)
    return(ans)
for case in range(T):
    S,L,R =input().split()
    L =int(L)
    R = int(R)
    ans = 0
    print(cal(R,S)-cal(L-1,S))