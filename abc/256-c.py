h1,h2,h3,w1,w2,w3  =map(int,input().split())
ans=0
for a in range(1,30):
    for b in range(1,30):
        for c in range(1,30):
            for d in range(1,30):
                e = h1-a-b
                f = h2-d-c
                h = w1-a-c
                g = w2-b-d
                i = w3-e-f
                if e>0 and f>0 and h>0 and g>0 and i>0:
                    ans+=1
if h1+h2+h3!=w1+w2+w3:
    ans=0
print(ans)