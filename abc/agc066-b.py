def dig(n):
    t = 0
    while n>0:
        t+=n%10
        n//=10
    return t
i = int(input())
k1 = dig(i)
k2 = dig(2*i)
k3 = dig(4*i)
k4 = dig(8*i)
k5 = dig(16*i)
if k1>k2>k3>k4>k5:
    print(i)
    
def dig(n):
    t = 0
    while n>0:
        t+=n%10
        n//=10
    return t
for i in range(1,10**6):
    k = i
    for j in range(7):
        if dig(k)<dig(k*2):
            break
        k*=2
    else:
        print(i)
N = int(input())
k = 0
for i in range(50,100):
    k*=10**100
    k+=5**i
ans = []
while k>0:
    ans.append(k%10)
    k//=10
ans.reverse()
print(*ans,sep="")
L = []
for i in range(50):
    L.append(dig(k)-dig(k*2))
    k*=2
print(L)