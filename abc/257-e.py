N = int(input())
C = list(map(int,input().split()))
times = N//min(C)
ans = []
temp=9
for i in reversed(range(times)):
    while N-C[temp-1]<min(C)*i:
        temp-=1
    ans.append(temp)
    N-=C[temp-1]
print(*ans,sep="")
