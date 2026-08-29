N=int(input())
A = list(map(int,input().split()))
ans = "Yes"
for i in range(N-2):
    if A[i]*A[i+2]!=A[i+1]*A[i+1]:
        ans = "No"
print(ans)