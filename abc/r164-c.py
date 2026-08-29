N = int(input())
A = []
B = []
ans = 0
for i in range(N):
    a,b = map(int,input().split())
    if a<b:
        B.append(b-a)
        ans+=a
    else:
        A.append(a-b)
        ans+=b
if len(A)==0:
    print(sum(B)+ans)
elif len(A)&1:
    if len(B)==0:
        print(sum(A)+ans-min(A))
    else:
    	print(sum(A)+sum(B)+ans-min(min(A),min(B)))
else:
    if len(B)==0:
        print(sum(A)+ans)
    else:
    	print(sum(A)+sum(B)+ans)