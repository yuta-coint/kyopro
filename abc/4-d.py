r,g,b = map(int,input().split())
def cr(s,t):
    x = -100
    a=0
    if x>=s and t>=x:
        a+=(x-s)*(x-s+1)//2
        a+=(t-x)*(t-x+1)//2
    elif x>=s:
        a+=(x-s)*(x-s+1)//2
        a-=(x-t)*(x-t-1)//2
    else:
        a-=(s-x)*(s-x-1)//2
        a+=(t-x)*(t-x+1)//2
    return(a)
def cr0(s,t):
    x = 0
    a=0
    if x>=s and t>=x:
        a+=(x-s)*(x-s+1)//2
        a+=(t-x)*(t-x+1)//2
    elif x>=s:
        a+=(x-s)*(x-s+1)//2
        a-=(x-t)*(x-t-1)//2
    else:
        a-=(s-x)*(s-x-1)//2
        a+=(t-x)*(t-x+1)//2
    return(a)
def cr1(s,t):
    x = 100
    a=0
    if x>=s and t>=x:
        a+=(x-s)*(x-s+1)//2
        a+=(t-x)*(t-x+1)//2
    elif x>=s:
        a+=(x-s)*(x-s+1)//2
        a-=(x-t)*(x-t-1)//2
    else:
        a-=(s-x)*(s-x-1)//2
        a+=(t-x)*(t-x+1)//2
    return(a)
def center(x,s):
    l =(s-1)//2
    r = s//2
    a = l*(l+1)//2
    a+=r*(r+1)//2
    return(a)
ans = float("inf")
for p3 in range(-100,100+r+g+b):
    p2 = p3-b
    p1 = p2-g
    p0 = p1-r
    temp = cr(p0+1,p1)
    temp += cr0(p1+1,p2)
    temp += cr1(p2+1,p3)
    ans = min(ans,temp)
for p1 in range(-100+(r-1)//2,100+r+g+b):
    p2 = p1+g
    p3 = p2+b
    temp = center(-100,r)
    temp += cr0(p1+1,p2)
    temp += cr1(p2+1,p3)
    ans = min(ans,temp)
for p2 in range(-100-r-g,100-(b-1)//2):
    p1 = p2-g
    p0 = p1-r
    temp = cr(p0+1,p1)
    temp += cr0(p1+1,p2)
    temp += center(100,b)
    ans = min(ans,temp)
ma = min(99-(r-1)//2,99-(b-1)//2)
ma = ma*2+1
if 99-(r-1)//2!=99-(b-1)//2:
    ma+=1
if ma>=g:
    ans = center(-100,r)+center(0,g)+center(100,b)
    ans = min(ans,temp)
print(ans)


