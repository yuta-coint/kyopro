#和が10**8を超える組が何個あるか
N = int(input())
A = list(map(int,input().split()))
A.sort(reverse=True)
ans = sum(A)*(N-1)
#足したら10**8未満になる最小のind
cnt = N
for i in range(N):
    while A[cnt-1]+A[i]<10**8 and cnt>0:
        cnt-=1
    if cnt-i-1>0:
        ans -= (cnt-i-1)*(10**8)
print(ans)