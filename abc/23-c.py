import sys
input = sys.stdin.readline
r,c,k = map(int,input().split())
lr = [0 for i in range(r+1)]
lc = [0 for i in range(c+1)]
point = []
n = int(input())
for i in range(n):
    rn,cn=map(int,input().split())
    point.append([rn,cn])
    lr[rn]+=1
    lc[cn]+=1
ans = 0
for t in point:
    if lr[t[0]]+lc[t[1]]==k:
        ans-=1
    elif lr[t[0]]+lc[t[1]]==k+1:
        ans+=1
countr = [0 for i in range(n+1)]
countc = [0 for i in range(n+1)]
for i in range(1,r+1):
    countr[lr[i]]+=1
for i in range(1,c+1):
    countc[lc[i]]+=1
for i in range(n):
    if k-i<0 or k-i>n:
        continue
    ans += countr[i]*countc[k-i]
print(ans)
