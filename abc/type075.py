m = int(input())
def factorization(numa):
    arr = []
    hp = numa
    for i in range(2, int(-(-numa**0.5//1))+1):
        powa = 0
        while hp%i==0:
            hp //= i
            arr.append(i)
    if hp>1:
        arr.append(hp)
    return(arr)
fac = factorization(m)
if len(fac)==1:
    print(0)
else:
    print(len(bin(len(fac)-1))-2)