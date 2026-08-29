abc=list(map(int,input().split()))
m = sorted(abc)
if abc[1]==m[1]:
    print("Yes")
else:
    print("No")