T = int(input())
for i in range(T):
    a,s  =map(int,input().split())
    b=1
    for j in range(60):
        b*=2
        if a>>j & 1:
            s-=b
            if s<0:
                print("No")
                break
    else:
        if s&a == 0:
            print("Yes")
        else:
            print("No")
