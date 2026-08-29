H,W,D = map(int,input().split())
S = [input() for i in range(H)]
ans = 0
for x1 in range(H):
    for y1 in range(W):
        if S[x1][y1]=="#":
            continue
        for x2 in range(H):
            for y2 in range(W):
                if S[x2][y2]=="#":
                    continue
                temp = 0
                for i in range(H):
                    for j in range(W):
                        if S[i][j]=="#":
                            continue
                        if abs(i-x1)+abs(j-y1)<=D:
                            temp+=1
                            continue
                        if abs(i-x2)+abs(j-y2)<=D:
                            temp+=1
                if ans<temp:
                    ans = temp
print(ans)