#64bit整数であれば、1になっているbitの数を求めることができる！
def popcount(n):
  c=(n&0x5555555555555555)+((n>>1)&0x5555555555555555)
  c=(c&0x3333333333333333)+((c>>2)&0x3333333333333333)
  c=(c&0x0f0f0f0f0f0f0f0f)+((c>>4)&0x0f0f0f0f0f0f0f0f)
  c=(c&0x00ff00ff00ff00ff)+((c>>8)&0x00ff00ff00ff00ff)
  c=(c&0x0000ffff0000ffff)+((c>>16)&0x0000ffff0000ffff)
  c=(c&0x00000000ffffffff)+((c>>32)&0x00000000ffffffff)
  return c

N,D = map(int,input().split())
A = list(map(int,input().split()))
subset_ans=[]
for bits in range(1<<N):
    banned = 0
    for i in range(N):
        if (bits>>i)&1:
            banned|=A[i]
    subset_ans.append(1<<(D-popcount(banned)))
ans = 0
for i in range(1<<N):
    if popcount(i)&1:
        ans+=subset_ans[i]
    else:
        ans-=subset_ans[i]
print(-ans)