H1,W1 = map(int,input().split())
A = [list(map(int,input().split())) for i in range(H1)]
H2,W2 = map(int,input().split())
B = [list(map(int,input().split())) for i in range(H2)]
ans = "No"
for x in range(1<<H1):
    cnt = 0
    for t in range(H1):
        if (x>>t)&1:
            cnt+=1
    if cnt!=H2:
        continue
    for y in range(1<<W1):
        cnt=0
        for t in range(W1):
            if (y>>t)&1:
                cnt+=1
        if cnt!=W2:
            continue
        temp = [[] for i in range(H2)]
        cnt = 0
        for i in range(H1):
            if not (x>>i)&1:
                continue
            for j in range(W1):
                if not (y>>j)&1:
                    continue
                temp[cnt].append(A[i][j])
            cnt+=1
        if temp==B:
            ans = "Yes"
print(ans)