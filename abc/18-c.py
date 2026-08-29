import sys
input = sys.stdin.readline
r,c,k = map(int,input().split())
s = [input() for i in range(r)]
sums = [[0] for i in range(r)]
for i in range(r):
    for j in range(c):
        if s[i][j]=="x":
            sums[i].append(sums[i][-1]+1)
        else:
            sums[i].append(sums[i][-1])
#print(sums)
ans = 0
for ri in range(k-1,r-k+1):
    for ci in range(k-1,c-k+1):
        for i in range(1,k):
            if sums[ri-i][ci+k-i]!=sums[ri-i][ci-k+1+i]:
                break
            if sums[ri+i][ci+k-i]!=sums[ri+i][ci-k+1+i]:
                break
        else:
            if sums[ri][ci+k]==sums[ri][ci-k+1]:
                ans+=1
                #print(ri,ci)
print(ans)
        