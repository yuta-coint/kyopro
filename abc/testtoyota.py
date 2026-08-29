R = 100
for a in range(1,R):
    for b in range(a+1,1+R):
        if a%(a^b)==0 and b%(a^b)==0:
            if a^b==3:
                print(a//(a^b),b//(a^b),a^b)
L,R = map(int,input().split())
ans = 0
for a in range(L,R):
    for b in range(a+1,1+R):
        if a%(a^b)==0 and b%(a^b)==0:
            ans+=1
print(ans)