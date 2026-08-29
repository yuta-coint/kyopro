N,A,B = map(int,input().split())
if A<=B:
    ans = max(N-A+1,0)
else:
    p = N//A
    q = N%A
    if p==0:
        ans=0
    else:
        ans = (p-1)*B+min(q+1,B)
print(ans)
