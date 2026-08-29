x1,y1,x2,y2 = map(int,input().split())
absp = (x2-x1)**2 + (y2-y1)**2
q = int(input())
for i in range(q):
    x,y = map(int,input().split())
    son = (x-x1)*(x2-x1)+(y-y1)*(y2-y1)
    pjx = (((x-x1)*(x2-x1)+(y-y1)*(y2-y1)) * (x2-x1))/absp
    pjy = (((x-x1)*(x2-x1)+(y-y1)*(y2-y1)) * (y2-y1))/absp
    pjx+=x1
    pjy+=y1
    print(pjx,pjy)