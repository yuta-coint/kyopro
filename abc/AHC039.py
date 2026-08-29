def ruiseki(x0,x1,y0,y1):
    rui_LU = [[0 for i in range((y1-y0)//2)] for j in range((x1-x0)//2)]
    rui_RU = [[0 for i in range((y1-y0)//2)] for j in range((x1-x0)//2)]
    rui_LD = [[0 for i in range((y1-y0)//2)] for j in range((x1-x0)//2)]
    rui_RD = [[0 for i in range((y1-y0)//2)] for j in range((x1-x0)//2)]
N = int(input())
M = 10**5
haba = 100
masu = M//haba
sea = [[0 for i in range(M//haba)] for j in range(M//haba)]
def calc(n,s):
    ans = 0
    for i in range(M//haba):
        for j in range(M//haba):
            ans+=s[i][j]*n[i][j]
    return ans
for i in range(N):
    x,y = map(int,input().split())
    if x==10**5:
      x-=1
    else:
      y-=1
    sea[x//haba][y//haba]+=1
for i in range(N):
    x,y = map(int,input().split())
    sea[x//haba][y//haba]-=1
sea_sum = [[0 for i in range(masu+1)] for j in range(masu+1)]
for i in range(masu):
    for j in range(masu):
        sea_sum[i+1][j+1]=sea_sum[i][j+1]+sea_sum[i+1][j]-sea_sum[i][j]+sea[i][j]
s,t = 0,0
for i in range(masu+1):
    for j in range(masu+1):
        if sea_sum[i][j]>sea_sum[s][t]:
            s,t = i,j
ura_sum = [[0 for j in range(t+1)] for i in range(s+1)]
for i in reversed(range(s)):
    for j in reversed(range(t)):
        ura_sum[i][j]=ura_sum[i+1][j]+ura_sum[i][j+1]-ura_sum[i+1][j+1]+sea[i][j]
s1,t1 = 0,0
#print(ura_sum)
for i in range(s+1):
    for j in range(t+1):
        if ura_sum[i][j]>ura_sum[s1][t1]:
            s1,t1 = i,j
print(4)
print(s1*haba,t1*haba)
print(s*haba-1,t1*haba)
print(s*haba-1,t*haba-1)
print(s1*haba,t*haba-1)
