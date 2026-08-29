T = int(input())
for case in range(T):
    N = int(input())
    S = input()
    cnt = 0
    flag = -1
    flag2 = -1
    for i in range(N):
        if S[i]=="1":
            cnt+=1
            if flag==-1:
                flag = i
            flag2 = i
    if cnt==2:
        if flag2-flag>1:
            print(1)
        elif N<=3:
            print(-1)
        elif S == "0110":
            print(3)
        else:
            print(2)
    else:
        if cnt&1:
            print(-1)
        else:
            print(cnt//2)