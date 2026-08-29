N = int(input())
A = list(map(int,input().split()))
size_sum = sum(A)
if size_sum%10!=0:
    print("No")
    exit()
A+=A
size_sum//=10
cake = 0
l = 0
for i in range(2*N):
    cake+=A[i]
    while cake>size_sum:
        cake-=A[l]
        l+=1
    if cake==size_sum:
        print("Yes")
        break
else:
    print("No")
