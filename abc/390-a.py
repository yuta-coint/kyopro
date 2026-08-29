A = list(map(int,input().split()))
tento = 0
for i in range(5):
    for j in range(i+1,5):
        if A[i]>A[j]:
            tento += 1
if tento == 1:
    print("Yes")
else:
    print("No")