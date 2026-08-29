T = int(input())
for _ in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    B = list(map(int,input().split()))
    if A == B:
        print("Yes")
        continue
    X = [A[0]]
    Y = [B[0]]
    for i in range(1,N):
        if A[i]!=A[i-1]:
            X.append(A[i])
        if B[i]!=B[i-1]:
            Y.append(B[i])
    if len(X)>1 and X[0]==X[-1]:
        X.pop()
    if len(Y)>1 and Y[0]==Y[-1]:
        Y.pop()
    ly = len(Y)
    lx = len(X)
    #print(X)
    #print(Y)
    if lx<ly or ly==N:
        print("No")
        continue
    ans = "No"
    for s in range(lx):
        key = 0
        for i in range(lx):
            if key == ly:
                break
            if X[(s+i)%lx]==Y[key]:
                key+=1
        if key == ly:
            ans = "Yes"
    print(ans)