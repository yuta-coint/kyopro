def factorization(n):
    arr = []
    hp = n
    for i in range(2, int(-(-n**0.5//1))+1):
        pow = 0
        while hp%i==0:
            hp //= i
            pow += 1
        if pow>0:
            arr.append([i, pow])
    if hp>1:
        arr.append([hp,1])
    return(arr)
T = int(input())
for i in range(T):
    N = int(input())
    fc = factorization(N)
    if len(fc)==1:
        print("No")
        continue
    s = 0
    for p,cnt in fc:
        s+=p**cnt
    if s<=N:
        print("Yes")
    else:
        print("No")


