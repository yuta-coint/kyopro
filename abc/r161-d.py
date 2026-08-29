N,D = map(int,input().split())
if D*N>N*(N-1)//2:
    print(-1)
    exit()
print("Yes")
for x in range(N):
    for j in range(1,1+D):
        y = (x+j)%N
        if x<y:
            print(x+1,y+1)
        y=(x-j)%N
        if x<y:
            print(x+1,y+1)