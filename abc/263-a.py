A = list(map(int,input().split()))
A.sort()
if A[0]==A[1] and A[1]!=A[2] and A[2]==A[4]:
    print("Yes")
elif A[0]==A[2] and A[2]!=A[3] and A[3]==A[4]:
    print("Yes")
else:
    print("No")
