N,M = map(int,input().split())
if N==1:
    print(M)
    exit()
if N==2:
    print(0,M)
    exit()
if N==3:
    print(-10**7,10**7-1,M+1)
    exit()
L = [0,1,3,4,9,10,12,13]
L2 = []
p = 27
L3 = []
for i in L:
    a1 = i*(p**4)
    for j in L:
        a2 = a1+j*(p**3)
        for k in L:
            a3  = a2+k*p*p
            for h in L:
                a4 = a3+h*p
                for g in L:
                    L3.append(a4+g)
L3 = L3[:N-1]
s = sum(L3)+10**7
k = (s-M)%(N-1)
s-=k
k2 = (s-M)//(N-1)
ans = [L3[i]-k2 for i in range(N-1)]
ans.append(10**7-k)
print(*ans)