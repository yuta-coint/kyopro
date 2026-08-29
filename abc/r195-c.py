T = int(input())
big  = 10**8
for _ in range(T):
    R,B = map(int,input().split())
    if R%2==1:
        print("No")
        continue
    if R==0 and B%2==1:
        print("No")
        continue
    print("Yes")
    if R==0 and B==2:
        print("B",2,2)
        print("B",1,1)
    elif R==2 and B==0:
        print("R",2,2)
        print("R",2,1)
    elif B%2==1:
        N = (B-1)//2
        M = (R-1)//2
        for i in range(N+1):
            print("B",big+i,big+i)
        for i in reversed(range(N)):
            print("B",big+i+2,big+i)
        print("R",big+1,big-1)
        for i in range(M+1):
            print("R",big-i,big-1)
        for i in reversed(range(1,M+1)):
            print("R",big-i,big+0)
    elif R==0:
        N = (B-2)//2
        for i in range(N+1):
            print("B",big+i,big+i)
        for i in reversed(range(N)):
            print("B",big+i+2,big+i)
        print("B",big+1,big-1)
    elif B==0:
        N = (R-2)//2
        for i in range(N+1):
            print("R",big+i,big+0)
        for i in reversed(range(N+1)):
            print("R",big+i,big-1)
    else:
        N=  (B-2)//2
        M = (R-2)//2
        for i in range(N+1):
            print("B",big+i,big+i)
        for i in reversed(range(N)):
            print("B",big+i+2,big+i)
        print("B",big+1,big-1)
        for i in range(M+1):
            print("R",big-i,big-2)
        print("R",big-M,big-1)
        for i in reversed(range(1,M+1)):
            print("R",big-i,big+0)