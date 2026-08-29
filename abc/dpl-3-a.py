h,w=map(int,input().split())
c = []
for i in range(h):
    ci=list(map(int,input().split()))
    c.append(ci)
ans = [[] for i in range(h)]
for j in range(w):
    ans[0].append(1-c[0][j])
for i in range(1,h):
    ans[i].append(1-c[i][0])
    for j in range(1,w):
        if c[i][j]==0:
            ans[i].append(min(ans[i-1][j],ans[i][j-1],ans[i-1][j-1])+1)
        else:
            ans[i].append(0)
a = 0
for i in range(h):
    a = max(a,max(ans[i]))
print(a*a)
            

