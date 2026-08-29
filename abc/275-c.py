from itertools import product
L  = [input() for j in range(9)]
ans = 0
def dist(p,q,r,s):
    return((p-r)**2+(q-s)**2)
def is_square(a1,a2,b1,b2,c1,c2,d1,d2):
    if a1==c1 and a2==c2:
        return(False)                       
    elif b1==d1 and b2==d2:
        return(False)     
    elif a1==b1 and a2==b2:
        return(False)     
    if dist(a1,a2,b1,b2)==dist(b1,b2,c1,c2) and dist(a1,a2,d1,d2)==dist(b1,b2,c1,c2) and dist(c1,c2,b1,b2)==dist(d1,d2,c1,c2):
        if dist(a1,a2,c1,c2)==dist(b1,b2,d1,d2):
            if L[a1][a2]=="#" and L[b1][b2]=="#" and L[c1][c2]=="#" and L[d1][d2]=="#": 
                return(True)
    return(False)
Nine = [i for i in range(9)]

for a,b,c,d,e,f,g,h in product(Nine,Nine,Nine,Nine,Nine,Nine,Nine,Nine):
    if is_square(a,b,c,d,e,f,g,h):
        ans+=1
print(ans//8)