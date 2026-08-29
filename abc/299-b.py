N,T  =map(int,input().split())
C = list(map(int,input().split()))
R=  list(map(int,input().split()))
ans = -1
ma = -1
for i in range(N):
    if C[i]==T:
        if R[i]>ma:
            ma = R[i]
            ans = i+1
if ans>=0:
    print(ans)
    exit()
for i in range(N):
    if C[i]==C[0]:
        if R[i]>ma:
            ma=R[i]
            ans=i+1
print(ans)