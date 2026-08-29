#成人した段階で、何人目まで渡すかが決まり、最後の所持数も決まる
N=int(input())
A = list(map(int,input().split()))
tuika = [1 for i in range(N)]
temp = 0
ans = []
for i in range(N):
    A[i]+=temp
    if A[i]>=N-(i+1):
        ans.append(A[i]-N+(i+1))
    else:
        ans.append(0)
        tuika[i+A[i]]-=1
    temp += tuika[i]
print(*ans)