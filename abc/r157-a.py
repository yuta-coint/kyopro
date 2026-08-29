N,A,B,C,D = map(int,input().split())
if abs(B-C)>=2:
    print("No")
    exit()
if B ==0 and C == 0 and A*D!=0:
    print("No")
    exit()
print("Yes")