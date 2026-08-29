N,X,Y =map(int,input().split())
Red = 1
Blue = 0
for i in range(N-1):
    Red,Blue = Red+Blue+Red*X,(Blue+Red*X)*Y
print(Blue)
