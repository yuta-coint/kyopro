a,b = map(int,input().split())
def accum(n):
    if n%4==3:
        return(0)
    elif n%4==0:
        return(n)
    elif n%4==1:
        return(n^(n-1))
    else:
        return(n^(n-1)^(n-2))
print(accum(b)^accum(a-1))