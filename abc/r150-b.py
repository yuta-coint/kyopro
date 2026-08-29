T = int(input())
for _ in range(T):
    A,B = map(int,input().split())
    ans = float("inf")
    if A<5*(10**4):
        for x in range(A):
            if B%(A+x)==0:
                temp = x
            else:
                temp = x+A+x-B%(A+x)
            if ans>temp:
                ans=temp
                #print(A+x,B+ans-x)
    else:
        if A>B:
            ans = A-B
        for k in range(1,3*(10**4)):
            if B%k==0:
                x = (B//k)-A
            else:
                x = (B//k)-A+1
            #if k==6:
                #print(x)
            if x<0:
                x=0
            y = k*(A+x)-B
            if ans>x+y:
                #print(ans)
                ans=x+y
    print(ans)
