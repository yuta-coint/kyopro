knight = [(1,2),(1,-2),(-1,2),(-1,-2),(2,1),(2,-1),(-2,1),(-2,-1)]
x1,y1,x2,y2 = map(int,input().split())
r = []
for i in range(8):
    r.append((x1+knight[i][0],y1+knight[i][1]))
    r.append((x2+knight[i][0],y2+knight[i][1]))
if len(set(r))==16:
    print("No")
else:
    print("Yes")