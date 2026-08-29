N = int(input())
a = list(map(int,input().split()))
if N&1:
    if a[N-1]-a[N-2]==1 and not a[N-1]&1:
        print("Bob")
    else:
        print("Alice")
else:
    if a[N-1]-a[N-2]==1 and a[N-1]&1:
        print("Bob")
    else:
        print("Alice")
