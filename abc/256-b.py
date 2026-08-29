n =int(input())
A = list(map(int,input().split()))
P=0
base = [False,False,False,False]
for i in range(n):
    base[0]=True
    for j in reversed(range(4)):
        if base[j]:
            if j+A[i]>=4:
                P+=1
            else:
                base[j+A[i]]=True
            base[j]=False
print(P)