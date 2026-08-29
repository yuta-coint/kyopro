N = int(input())
A = list(map(int,input().split()))
m = (N+1)//2
A.sort()
a1 = A[:m]
a2 = A[m:]
for i in range(m-1):
    if a2[i]==a1[i] or a2[i]==a1[i+1]:
        print("No")
        exit()
print("Yes")