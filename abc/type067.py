def operation(n):
    n = int(n,8)
    new = ""
    while n>0:
        if n%9==8:
            new+="5"
        else:
            new+=str(n%9)
        n//=9
    new = new[::-1]
    return(new)
N,K = map(int,input().split())
N = str(N)
if N != "0":
    for i in range(K):
        N = operation(N)
    print(N)
else:
    print(0)