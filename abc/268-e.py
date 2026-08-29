N = int(input())
p = list(map(int,input().split()))
cnt = [0 for i in range(N)]
for i in range(N):
    p[i] = (p[i]-i)%N
    cnt[p[i]]+=1
up_sum = 0
middle_sum = 0
up_cnt = 0
middle_cnt = 0
for i in range(N//2+1):
    middle_sum+=cnt[i]*i
    middle_cnt+=cnt[i]
for i in range(N//2+1,N):
    up_sum+=i*cnt[i]
    up_cnt+=cnt[i]
ans = float('inf')
for x in range(N):
    #print(middle_cnt,middle_sum,up_cnt,up_sum)
    temp=middle_sum-x*middle_cnt+up_cnt*N-up_sum+x*up_cnt
    if ans>temp:
        ans = temp
    middle_cnt+=-cnt[x]+cnt[(x+1+N//2)%N]
    middle_sum+=-cnt[x]*x+cnt[(x+1+N//2)%N]*(x+1+N//2)
    up_cnt+=-cnt[(x+1+N//2)%N]+cnt[x]
    up_sum+=-cnt[(x+1+N//2)%N]*(x+1+N//2)+cnt[x]*(x+N)
print(ans)