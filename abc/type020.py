a,b,c = map(int,input().split())
k = 1
if c==1:
    print("No")
else:
    for i in range(b):
        k*=c
        if k>a:
            print("Yes")
            break
    else:
        print("No")
