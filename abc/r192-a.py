N = int(input())
A = list(map(int,input().split()))
if N%2==1:
    if sum(A)==0:
        print("No")
    else:
        print("Yes")
elif N%4==0:
    print("Yes")
else:
    o = False
    e = False
    for i in range(N):
        if A[i]==1:
            if i%2==0:
                e = True
            else:
                o = True
    if o and e:
        print("Yes")
    else:
        print("No")