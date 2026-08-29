n,x,y = map(int,input().split())
a = list(map(int,input().split()))
tempx = n
tempy = n
tempout = n
ans = 0
for i in reversed(range(n)):
    if a[i]==x:
        tempx = i
    if a[i]==y:
        tempy =i
    if a[i]>x or a[i]<y:
        tempout = i
    #print(tempx,tempy,tempout)
    ans += max(tempout-max(tempy,tempx),0)
print(ans)



