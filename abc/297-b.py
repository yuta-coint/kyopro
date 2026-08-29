S = list(input())
x = -1
r1=-1
for i in range(8):
    if S[i]=="B":
        if x==-1:
            x=i
        else:
            y=i
    if S[i]=="R":
        if r1==-1:
            r1=i
        else:
            r2=i
    if S[i]=="K":
        k=i
if (x+y)&1 and (k-r1)*(k-r2)<0:
    print("Yes")
else:
    print("No")
