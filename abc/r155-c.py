N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
from copy import copy
check_a,check_b = A.copy(),B.copy()
check_a.sort()
check_b.sort()
if check_b!=check_a:
    print("No")
    exit()
even_count = 0
for i in range(N):
    if A[i]%2==0:
        even_count+=1
if even_count==0:
    if A==B:
        print("Yes")
    else:
        print("No")
    exit()
#奇数で操作を始められるか
cutA = True
for i in range(N-1):
    if A[i]&1 and A[i+1]&1:
        cutA=False
for i in range(N-2):
    if A[i]&1 and A[i+2]&1:
        cutA=False
cutB = True
for i in range(N-1):
    if B[i]&1 and B[i+1]&1:
        cutB=False
for i in range(N-2):
    if B[i]&1 and B[i+2]&1:
        cutB=False
if cutA and cutB:
    boxA = []
    boxB = []
    for i in range(N):
        boxA.append(A[i])
        boxB.append(B[i])
        if A[i]&1:
            if B[i]!=A[i]:
                print("No")
                exit()
            if len(boxA)==3 and boxA[0]!=boxB[0]:
                print("No")
                exit()
            boxA.sort()
            boxB.sort()
            if boxA!=boxB:
                print("No")
                exit()
            boxA=[]
            boxB=[]
    if len(boxA)==2 and boxA[0]!=boxB[0]:
        print("No")
        exit()
    boxA.sort()
    boxB.sort()
    if boxA!=boxB:
        print("No")
        exit()
    print("Yes")
elif cutA or cutB:
    print("No")
else:
    if even_count==2:
        temp=0
        for i in range(N):
            if A[i]%2==0 and temp==0:
                e1=A[i]
                temp=1
            elif A[i]%2==0:
                e2=A[i]
        temp = 0
        for i in range(N):
            if B[i]%2==0 and temp==0:
                e3=B[i]
                temp=1
            elif B[i]%2==0:
                e4=B[i]
        if e1!=e3 or e2!=e4:
            print("No")
            exit()
    print("Yes")
