T = int(input())
for case in range(T):
    S = int(input())
    n=S//5
    if S%5==0 and n>=2:
        print("Yes")
        print(5*n-5,0,3*n-4,1,0,5)
    elif S%5==1 and n>=2:
        print("Yes")
        print(5*n-6,0,3*n-5,1,0,5)
    elif S%5==2 and n>=3:
        print("Yes")
        print(5*n-7,0,3*n-6,1,0,5)
    elif S%5==3 and n>=1:
        print("Yes")
        print(5*n-3,0,3*n-3,1,0,5)
    elif S%5==4 and n>=2:
        print("Yes")
        print(5*n-4,0,3*n-4,1,0,5)
    elif S==4:
        print("Yes")
        print(0,0,0,2,2,0)
    elif S==6:
        print("Yes")
        print(0,0,0,2,3,0)
    elif S==9:
        print("Yes")
        print(0,3,1,1,6,0)
    elif S==12:
        print("Yes")
        print(0,8,1,3,4,0)
    else:
        print("No")