T = int(input())
for i in range(T):
    n = int(input())
    if n==2 or n&1:
        print(-1)
    else:
        y = n//4
        x = (n+4)//6
        print(x,y)