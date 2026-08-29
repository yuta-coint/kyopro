N,K = map(int,input().split())
A = list(map(int,input().split()))
if sum(A)>=K:
    print("Yes")
    A.sort(reverse=True)
    print(*A)
else:
    if K<=0:
        print("No")
    else:
        print("Yes")
        A.sort()
        print(*A)
        