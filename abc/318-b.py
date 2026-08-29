sheet = [[0 for i in range(101)] for j in range(101)]
N= int(input())
for i in range(N):
    a,b,c,d  =map(int,input().split())
    for i in range(a,b):
        for j in range(c,d):
            sheet[i][j]|=1
ans =0
for i in range(101):
    ans+=sum(sheet[i])
print(ans)