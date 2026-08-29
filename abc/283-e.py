H,W=  map(int,input().split())
A = [list(map(int,input().split())) for i in range(H)]
ans =0
chk = []
for j in range(W):
    if A[0][j]==j&1:
        chk.append(0)
    else:
        ans+=1
        chk.append(1)
print(chk)
for i in range(1,H):
    push = 1
    if A[i][0]^chk[0]==i&1:
        push = 0
    else:
        ans+=1
    print(push)
    for j in range(1,W):
        if A[i][j]^push^chk[j]!=(i+j)&1:
            print(-1)
            exit()
print(min(ans,H+W-ans))

