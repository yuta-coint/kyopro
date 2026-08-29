points = []
for i in range(4):
    x,y = map(int,input().split())
    points.append((x,y))
points.append(points[0])
points.append(points[1])
ans = "Yes"
for i in range(4):
    ba = (points[i][0]-points[i+1][0],points[i][1]-points[i+1][1])
    bc = (points[i+2][0]-points[i+1][0],points[i+2][1]-points[i+1][1])
    if ba[0]*bc[1]>=ba[1]*bc[0]:
        ans="No"
print(ans)