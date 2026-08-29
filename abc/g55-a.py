t = int(input())
for i in range(t):
    l,r = map(int,input().split())
    if len(str(l))==len(str(r)):
        print(r-l+1)
    else:
        if len(str(l))+1<len(str(r)):
            l=10**(len(str(r))-2)
        b2 = 10**(len(str(r))-1)
        #print("l",b2)
        ban = max(r//10,r%b2)
        if r>=2*b2:
            ban = b2-1
        l = max(l,ban+1)
        print(r-l+1)

