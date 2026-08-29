n = int(input())
k,m = map(int,input().split())
if (n*k)%m==0:
    print("Yes")
else:
    print("No")