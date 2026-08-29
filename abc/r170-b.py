N = int(input())
A  =list(map(lambda x:int(x)-1,input().split()))
lastn = [-1 for i in range(10)]
chance = [-1 for i in range(10)]
left = [N for i in range(N)]
solved = 0
for i in range(N):
    #来てほしいものが来ているか
    s = chance[A[i]]
    if s>=solved:
        for j in range(solved,s+1):
            left[j]=i
        solved = s+1
    for j in range(10):
        if 0<=A[i]*2-j<10:
            if chance[A[i]*2-j]<lastn[j]:
                chance[A[i]*2-j]=lastn[j]
    lastn[A[i]] = i
ans = 0
for i in range(N):
    ans += N-left[i]
print(ans)