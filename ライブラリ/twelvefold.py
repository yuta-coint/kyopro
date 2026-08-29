n,k = map(int,input().split())
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
#区別できるボールを区別できる箱に一個以上ずつ入れる。
def twelvefold3(ball,box,mod):
    a = 0
    temp=1
    for i in range(box):
        temp*=(box-i)
        temp*=pow(i+1,mod-2,mod)
        temp%=mod
        if (box-i)&1:
            a+=(temp*pow(i+1,ball,mod))%mod
        else:
            a-=(temp*pow(i+1,ball,mod))%mod
        a%=mod
    return a
#区別できるボールを区別できない箱に一個以上ずつ入れる。
def sterling2(ball,box):
    b = twelvefold3(ball,box)
    for i in range(box):
        b*=bigpower(i+1,mod-2)
        b%=mod
    return(b)
print(sterling2(n,k))

def bell(ball,box):
    pre_bell = [1]
    #(-1)のn乗/iの階乗を足し合わせたやつ
    a = 1
    temp = 1
    for i in range(1,box+1):
        temp*=bigpower(i,mod-2)
        temp*=-1
        a+=temp
        pre_bell.append(a)
    #print(pre_bell)
    a = 0
    i_fac =1
    for i in range(1,box+1):
        i_fac*=bigpower(i,mod-2)
        a += (((pre_bell[box-i]*bigpower(i,ball))%mod)*i_fac)%mod
        a%=mod
    return(a)