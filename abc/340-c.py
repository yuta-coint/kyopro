N = int(input())
cnt1 = 0
cnt2 = 1
ans = 0
while N>1:
    if N==2:
        ans += cnt2*2
    else:
        ans += cnt2*N+cnt1*(N-1)
    if N&1:
        cnt1,cnt2 = 2*cnt1+cnt2,cnt2
        N=N+1
        N//=2
    else:
        cnt1,cnt2 = cnt1,cnt2*2+cnt1
        N//=2
print(ans)