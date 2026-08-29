T=int(input())
for _ in range(T):
    a1,a2,a3,a4,a5 = map(int,input().split())
    b1,b2,b3,b4,b5 = map(int,input().split())
    m = min(a5,b5)
    a5-=m
    b5-=m
    if a5>0:
        print("No")
        continue
    m = min(a4,b4)
    a4-=m
    b4-=m
    m = min(a4,b5)
    a4-=m
    b5-=m
    b1+=m
    if a4>0:
        print("No")
        continue
    m = min(a3,b3)
    b3-=m
    a3-=m
    m = min(a3,b5)
    a3-=m
    b5-=m
    b2+=m
    m = min(a3,b4)
    a3-=m
    b4-=m
    b1+=m
    if a3>0:
        print("No")
        continue
    b2 += b4*2+b5*2+b3
    b1+=b5+b3
    if b2>=a2 and b1+b2*2>=a1+a2*2:
        print("Yes")
    else:
        print("No")

            