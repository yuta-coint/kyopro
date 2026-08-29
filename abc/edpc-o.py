def popcount(n):
  c=(n&0x5555555555555555)+((n>>1)&0x5555555555555555)
  c=(c&0x3333333333333333)+((c>>2)&0x3333333333333333)
  c=(c&0x0f0f0f0f0f0f0f0f)+((c>>4)&0x0f0f0f0f0f0f0f0f)
  c=(c&0x00ff00ff00ff00ff)+((c>>8)&0x00ff00ff00ff00ff)
  c=(c&0x0000ffff0000ffff)+((c>>16)&0x0000ffff0000ffff)
  c=(c&0x00000000ffffffff)+((c>>32)&0x00000000ffffffff)
  return c
N=  int(input())
ans = [0 for i in range(1<<N)]
ans[0]=1
pop = [[] for i in range(N+1)]
#各popcount毎に分類する
for i in range(1<<N):
   pop[popcount(i)].append(i)
mod = 10**9+7
for i in range(1,1+N):
    a = list(map(int,input().split()))
    for j in range(N):
        if a[j]==0:
            continue
        for matches in pop[i]:
            if (matches>>j)&(a[j]):
                ans[matches]+=ans[matches-(1<<j)]
                ans[matches]%=mod
print(ans[-1])