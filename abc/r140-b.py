def main():
    N = int(input())
    s = input()
    ability = [-1 for i in range(N)]
    cnta = 0
    cntc = 0
    for i in range(N):
        if s[i]=="A":
            cnta+=1
        elif s[i]=="R":
            ability[i]= cnta
            cnta=0
        else:
            cnta=0
    for i in reversed(range(N)):
        if s[i]=="C":
            cntc+=1
        elif s[i]=="R":
            ability[i]= min(ability[i],cntc)
            cntc = 0
        else:
            cntc=0
    q = []
    one = 0
    for i in range(N):
        if ability[i]<=0:
            continue
        if ability[i]==1:
            one+=1
        else:
            q.append(ability[i])
    q.sort()
    idm = len(q)
    ans = 0
    id = 0
    while True:
        if one>0 and id<idm:
            if q[id]==2:
                id+=1
                one+=1
            else:
                q[id]-=1
            one-=1
            ans+=2
        elif id<idm:
            ans+=2
            id+=1
        else:
            ans+=one
            break
    print(ans)
main()



