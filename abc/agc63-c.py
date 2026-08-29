N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))

d = {}
for i in range(N):
    if A[i] in d:
        if d[A[i]]!=B[i]:
            print("No")
            exit()
    else:
        d[A[i]]=B[i]
AB = [(A[i],B[i]) for i in range(N)]
AB = list(set(AB))
N = len(AB)
AB.sort(reverse=True)
big = 10**12
print("Yes")
print(N)
if N==1:
    print(big%(big+A[0]-B[0]),big+A[0]-B[0])
    exit()
A = [AB[i][0] for i in range(N)]
B = [AB[i][1]+(N-i-1)*2*big for i in range(N)]
#print(A,B)
for i in range(N):
    if i==0:
        x,y = big*(10**4)+(B[N-1]-B[0]-A[N-1])%big,big*(10**4)+(B[N-1]-B[0]-A[N-1])%big+A[0]
    elif i==N-1:
        x,y = B[N-2],big
    else:
        x,y = B[i-1]-B[i],A[i]+B[i-1]-B[i]
    print(x%y,y)
    for j in range(N):
        A[j]=(A[j]+x)%y
    #print(A)
#print(A)