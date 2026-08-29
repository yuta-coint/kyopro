A = list(map(int,input().split()))
B = [0 for i in range(5)]
for i in range(4):
    B[A[i]]+=1
ans = 0
for i in range(5):
    ans+=B[i]//2
print(ans)