M,D = map(int,input().split())
y,m,d = map(int,input().split())
if d<D:
    d+=1
elif m<M:
    d=1
    m+=1
else:
    d=1
    m=1
    y+=1
print(y,m,d)

