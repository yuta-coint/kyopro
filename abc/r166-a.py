T = int(input())
for case in range(T):
    N,X,Y = input().split()
    N = int(N)
    flag = 0
    cut = [-1]
    for i in range(N):
        if Y[i]=="C":
            if X[i]=="C":
                cut.append(i)
            else:
                flag = 1
                break
    cut.append(N)
    if flag == 1:
        print("No")
        continue
    ans = "Yes"
    for t in range(len(cut)-1):
        if cut[t+1]-cut[t]<=1:
            continue
        XA = 0
        XB = 0
        YA = 0
        YB = 0
        for i in range(cut[t]+1,cut[t+1]):
            if X[i]=="A":
                XA+=1
            elif X[i]=="B":
                XB+=1
            if Y[i]=="A":
                YA+=1
            elif Y[i]=="B":
                YB+=1
        if XA>YA or XB>YB:
            ans = "No"
            break
        mX = []
        mY = []
        cnt = YA-XA
        for i in range(cut[t]+1,cut[t+1]):
            if X[i]=="A":
                mX.append(i)
            elif X[i]=="C":
                if cnt>0:
                    mX.append(i)
                    cnt-=1
            if Y[i]=="A":
                mY.append(i)
        for i in range(len(mX)):
            if mX[i]>mY[i]:
                ans = "No"
        if ans == "No":
            break
    print(ans)