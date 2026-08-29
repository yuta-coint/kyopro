H,W,N = map(int,input().split())
A = list(map(int,input().split()))
choco = [0 for i in range(26)]
for i in range(25):
    if (H>>i)&1 and (W>>i)&1:
        choco[i]=(H>>i)+(W>>i)-1
    elif (H>>i)&1:
        choco[i] = W>>i
    elif (W>>i)&1:
        choco[i] = H>>i
choco[25] = (W>>25)*(H>>25)
print(choco)
A.sort()
for i in range(N):
    if choco[A[i]]>0:
        choco[A[i]]-=1
    else:
        kuri = 30
        for j in range(A[i]+1,26):
            if choco[j]>0:
                kuri = j
                break
        if kuri==30:
            print("No")
            exit()
        choco[kuri]-=1
        for j in range(A[i],kuri):
            choco[j]+=3
print("Yes")
print(choco)