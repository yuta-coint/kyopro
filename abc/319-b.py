N = int(input())
ans = []
for i in range(N+1):
    for j in range(1,10):
        if N%j==0 and i%(N//j)==0:
            ans.append(j)
            break
    else:
        ans.append("-")
print(*ans,sep="")