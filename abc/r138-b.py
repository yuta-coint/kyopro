N=int(input())
a = list(map(int,input().split()))
ans = "Yes"
cnt=N
for i in range(N-1):
    if a[i+1]==a[i]:
        cnt=i
        break
cut = 0
for i in range(cnt,N-1):
    if a[i]!=a[i+1]:
        cut+=1
if cnt<cut:
    ans = "No"
if a[0]==1:
    ans = "No"
print(ans)