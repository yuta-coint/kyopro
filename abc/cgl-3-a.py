N = int(input())
points = [tuple(map(int,input().split())) for i in range(N)]
def area(polygon,N):
    ans = 0
    for i in range(1,N-1):
        ans+=(polygon[i][0]-polygon[0][0])*(polygon[i+1][1]-polygon[0][1])-(polygon[i][1]-polygon[0][1])*(polygon[i+1][0]-polygon[0][0])
    return(ans/2)
print(area(points,N))