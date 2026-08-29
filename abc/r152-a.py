N,L=map(int,input().split())
A = list(map(int,input().split()))
one = 0
long_seat = L
ans = "Yes"
for i in range(N):
    if long_seat==0:
        if A[i]==2:
            ans = "No"
    elif long_seat==2:
        long_seat=0
    else:
        long_seat-=1+A[i]
        if long_seat==1:
            long_seat=0
print(ans)
