a,b = map(int,input().split())
def ban(n):
    l = len(str(n))
    ans = 0
    for i in reversed(range(l)):
        digit=n//(10**i)
        n-=digit*(10**i)
        if digit%5==4:
            ans+=(digit-digit//5)*(8**(i))-1
            break
        ans+=(digit-digit//5)*(8**(i))
    return(ans)
print(b-a+1-ban(b)+ban(a-1))


