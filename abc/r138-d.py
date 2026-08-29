n,k = map(int,input().split())
gray = []
if k&1 and k<n:
    for i in range(1<<(k+1)):
        gray.append(i^(i>>1))
    for i in range(1,1<<(k+1),2):
        gray[i]=(1<<(k+1))-1-gray[i]
    for b in range(k+1,n):
        id = 1<<(b-k)
        id = id^(id>>1)
        for i in range(2**(b)):
            para = 2**(k-1)-1
            gray.append(gray[1<<b-(i+1)]^(1<<(k-1)-1)^(1<<b))
    print("Yes")
    print(*gray)
elif n==1:
    print("Yes")
    print(0,1)

else:
    print("No")