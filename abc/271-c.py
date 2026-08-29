N = int(input())
A=list(map(int,input().split()))
A.sort()
sA = set(A)
ma = 3*(10**5)+1
mi = 0
while mi+1<ma:
    med = (ma+mi)//2
    cnt=0
    for i in range(1,med+1):
        if i in sA:
            cnt+=1
    if cnt+(N-cnt)//2 >= med:
        mi=med
    else:
        ma=med
print(mi)