h,w = map(int,input().split())
c = []
check = [[False for j in range(w)] for i in range(h)]
for i in range(h):
    ci = input()
    c.append(ci)
ans = 1
check[0][0]=True
for i in range(h):
    for j in range(w):
        if c[i][j]==".":
            if i>0:
                if check[i-1][j]==True:
                    check[i][j]=True
                    ans = max(ans,i+j+1)
            if j>0:
                if check[i][j-1]==True:
                    check[i][j]=True
                    ans = max(ans,i+j+1)
print(ans)