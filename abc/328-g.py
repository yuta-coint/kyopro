#64bit整数であれば、1になっているbitの数を求めることができる！
def popcount(n):
  c=(n&0x5555555555555555)+((n>>1)&0x5555555555555555)
  c=(c&0x3333333333333333)+((c>>2)&0x3333333333333333)
  c=(c&0x0f0f0f0f0f0f0f0f)+((c>>4)&0x0f0f0f0f0f0f0f0f)
  c=(c&0x00ff00ff00ff00ff)+((c>>8)&0x00ff00ff00ff00ff)
  c=(c&0x0000ffff0000ffff)+((c>>16)&0x0000ffff0000ffff)
  c=(c&0x00000000ffffffff)+((c>>32)&0x00000000ffffffff)
  return c
cnt = 0
N,C = map(int,input().split())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
#隣り合っていたらC点ボーナスみたいな感じか
#右端がいくらかと前の方を占有している集合
dp = [10**24 for sets in range(1<<N)]
#足す元のやつがなくなるとC節約できる。なんやこのテク
dp[0]=-C
for S in range(1,1<<N):
    pc = popcount(S)
    for new in range(N):
        if (S>>new)&1==0:
            continue
        old = S
        j = pc
        stock = C
        for newcut in reversed(range(new+1)):
            if (S>>newcut)&1==0:
                break
            old -= (1<<newcut)
            j-=1
            stock += abs(A[newcut]-B[j])
            if dp[S]>dp[old]+stock:
                dp[S] = dp[old]+stock
                cnt+=1
print(dp[-1])