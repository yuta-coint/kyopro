T = int(input())
for _ in range(T):
    N,K = map(int,input().split())
    S="0"+input()+"0"
    l=N+1
    for i in range(N+2):
        if S[i]=="1":
            l=i
            break
    r = 0
    for i in reversed(range(N+2)):
        if S[i]=="1":
            r=i
            break
    #1がない
    if l>r:
        cnt=0
        temp = 0
        for i in range(N+2):
            if S[i]=="0":
                #print(cnt)
                if cnt==K:
                    temp+=1
                elif cnt>K:
                    temp+=2
                cnt=0
            else:
                cnt+=1
        #print(temp)
        if temp==1:
            print("Yes")
        else:
            print("No")
        continue
    f = 0
    for i in range(l,r+1):
        if S[i]=="0":
            f=1
    if f==1:
        print("No")
        continue
    if r-l+1==K:
        print("Yes")
        continue
    for i in reversed(range(l)):
        if S[i]=="0":
            l2=i
            break
    for i in range(r,N+2):
        if S[i]=="0":
            r2=i
            break
    if r2-l2-1==K:
        print("Yes")
    elif r2-l2-1>K:
        if l-1==l2 and r-l2<=K:
            print("Yes")
        elif r+1==r2 and r2-l<=K:
            print("Yes")
        else:
            print("No")
    else:
        print("No")

