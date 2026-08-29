#列も行も違うます
#列が同じ
#列が違う
mod = 998244353
h,w,k = map(int,input().split())
a,b,c,d = 0,0,0,0
x1,y1,x2,y2 = map(int,input().split())
if x1==x2 and y1==y2:
    d=1
elif x1==x2:
    c=1
elif y1==y2:
    b=1
else:
    a=1
for i in range(k):
    tempa = ((w-1)*b)%mod+((h-1)*c)%mod+((w+h-4)*a)%mod
    tempa%=mod
    tempb = a+((h-1)*d)%mod+((h-2)*b)%mod
    tempb%=mod
    tempc = a+((w-1)*d)%mod+((w-2)*c)%mod
    tempc%=mod
    tempd = b+c
    tempd%=mod
    a,b,c,d = tempa,tempb,tempc,tempd
print(d)
#print(a,b,c,d)
