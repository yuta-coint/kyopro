mod = 10**9+7
##mの(pow乗)
def bigpower(base,pow):
    num = 1
    for i in reversed(range(len(bin(pow)))):
        num = num*num%mod
        if pow>>i & 1:
            num = num*base%mod
        i+=1
    return(num)

###組み合わせをmodで割った余り（pCq、計算量pq）
def pcq(p,q):
    com = 1
    for i in range(q):
        com *= bigpower(i+1,mod-2)
        com *= p-i
        com %= mod
    return(com)

h,w,a,b = map(int,input().split())
if h-a>w-b:
    h,w = w,h
    a,b = b,a
p = pcq(h-a-1+b,b)
q = pcq(w-b-1+a,a)
ans =p*q%mod
for i in range(1,h-a):
    p *= bigpower(b+i,mod-2)
    p *= h-a-i
    p%=mod
    q *= bigpower(a+i,mod-2)
    q *= w-b-i
    q%=mod
    ans+=p*q%mod
    ans%=mod
print(ans)