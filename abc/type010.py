n = int(input())
ans = [[0],[0]]
for i in range(n):
    c,p = map(int,input().split())
    ans[c-1].append(ans[c-1][-1]+p)
    ans[2-c].append(ans[2-c][-1])
q = int(input())
for i in range(q):
    l,r = map(int,input().split())
    print(ans[0][r]-ans[0][l-1],ans[1][r]-ans[1][l-1])
