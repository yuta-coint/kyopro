n,m,k = map(int,input().split())
mod = 998244353
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
W = [int(input()) for i in range(n)]
ans = bigpower(sum(W),k*mod-2)
sw = sum(W)
aw = (sw*bigpower(n,mod-2))%mod
#npow =[0]
#for i in range(1,2501):
#    npow.append(bigpower(i,k))
pm = 1
for i in range(n-m,n+1):
    temp = pcq(n,i)
    temp *= bigpower(n-1,k)
    temp %= mod
    c = ((n-i)*(n-i)*sw)%mod
    temp *=bigpower(c,k)
    temp %= mod
    ans+=temp
    ans%=mod
    pm*=-1
print(ans)



