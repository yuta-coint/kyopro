N=  int(input())
ans = []
for i in range(1,N+1):
    if i%3==0:
        ans.append("x")
    else:
        ans.append("o")
print(*ans,sep="")