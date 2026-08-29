A,B = map(int,input().split())
ans=0
while A!=B:
    if A>B:
        A,B=B,A
    if B%A==0:
        ans+=B//A-1
        break
    ans+=B//A
    B = B%A
print(ans)