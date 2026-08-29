def divisors(m):
    div = []
    for i in range(1, int(-(-m**0.5//1))+1):
        if m%i==0:
            div.append(i)
            if i!= m//i:
                div.append(m//i)
    return(set(div))
K = int(input())
d = divisors(K)
ans = 0
for a in d:
    for b in d:
        if a>b or K%(a*b)!=0:
            continue
        c = K//(a*b)
        if b<=c:
            #print(a,b,c)
            ans+=1
print(ans)
