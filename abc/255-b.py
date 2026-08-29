N,K = map(int,input().split())
A = list(map(int,input().split()))
A = set(A)
people = []
lights = []
for i in range(N):
    x,y = map(int,input().split())
    if i+1 in A:
        lights.append((x,y))
    else:
        people.append((x,y))
ans = 0
for p in people:
    temp = float("inf")
    for l in lights:
        #print(p,l)
        d = (p[0]-l[0])*(p[0]-l[0])+(p[1]-l[1])*(p[1]-l[1])
        temp = min(d,temp)
    #print(temp)
    ans = max(temp,ans)
print(ans**(1/2))