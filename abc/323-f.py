XA,YA,XB,YB,XC,YC = map(int,input().split())
if XB>XC:
    XA,XB,XC = -XA,-XB,-XC
if YB>YC:
    YA,YB,YC = -YA,-YB,-YC
if XB==XC:
    XA,XB,XC,YA,YB,YC=YA,YB,YC,XA,XB,XC
ans = 0
if YB==YC:
    #最後に押す分
    ans = XC-XB
    if YA==YB and XA>XB:
        ans+=2+(XA-XB+1)
    else:
        ans+=abs(XA-XB+1)+abs(YA-YB)
    print(ans)
    exit()
ans1 = 2+(XC-XB)+(YC-YB)
ans2 = 2+(XC-XB)+(YC-YB)
if YA==YB and XA>XB:
    ans1+=2+(XA-XB+1)
else:
    ans1+=abs(XA-XB+1)+abs(YA-YB)
if XA==XB and YA>YB:
    ans2+=2+(YA-YB+1)
else:
    ans2+=abs(YA-YB+1)+abs(XA-XB)
print(min(ans1,ans2))