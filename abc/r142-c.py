import sys
N = int(input())
ans = float("inf")
one=True
p1 = -1
p2 = -1
for i in range(3,N+1):
    print("?",1,i)
    sys.stdout.flush()
    t = int(input())
    print("?",2,i)
    sys.stdout.flush()
    s = int(input())
    ans = min(ans,s+t)
    if abs(s-t)!=1:
        one=False
    if t==1:
        p1=i
    elif s==1:
        p2=i
if p1!=-1 and p2!=-1:
    print("?",p1,p2)
    sys.stdout.flush()
    u=int(input())
    if u!=3:
        one = False
if one:
    ans=1
print("!",ans)
sys.stdout.flush()