N,M = map(int,input().split())
attacked = set()
knight = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
for i in range(M):
    a,b = map(int,input().split())
    for x,y in knight:
        if 1<=a+x<=N and 1<=b+y<=N:
            attacked.add((a+x)*10**12+(b+y))
print(N*N-len(attacked))