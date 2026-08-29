def divisors(m):
    if m==1:
        return([1])
    div = []
    for i in range(1, int(-(-m**0.5//1))+1):
        if m%i==0:
            div.append(i)
            if i!= m//i:
                div.append(m//i)
    return(sorted(div))
A,B = map(int,input().split())
if A==B:
    print(1)
    exit()
d = abs(A-B)
cand = divisors(d)
#print(cand)
from math import gcd
g = gcd(A,B)
key = cand.index(g)
l_cand = len(cand)
ans = 0
while True:
    temp = 10**16
    for i in reversed(range(key+1,l_cand)):
        if cand[i]%g>0:
            continue
        if B%cand[i]<temp:
            temp = B%cand[i]
            newg = cand[i]
            newkey = i
    if temp ==10**16:
        ans+= min(A//g,B//g)
        break
    ans+= temp//g
    A-=temp
    B-=temp
    g = newg
    key = newkey
    #print(g,ans)
print(ans)