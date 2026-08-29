loop = [1,3,2,6,4,5]
tri = [i*(i+1)//2 for i in range(2001)]
n = int(input())
t = 2000
ls = []
while n>0:
    if n>=tri[t]:
        ls.append(t+1)
        n-=tri[t]
    else:
        t-=1
ans1 = []
for i in range(len(ls)):
    for j in range(ls[i]):
        ans1.append(i)
ans2 = []
for i in range(len(ans1)-1):
    ans2.append(ans1[i+1]-ans1[i])
ans = []
for i in range(len(ans2)):
    if ans2[i]==0:
        ans.append(7)
    else:
        ans.append(loop[i%6])
print(*ans,sep="")
        


