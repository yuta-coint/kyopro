#ディーラーの値について確率を求めたい。
#前D個の平均が「その値を通る確率」になる
N,L,D = map(int,input().split())
deal = [1]
deal_sum = [0,1]
for i in range(1,L):
    if i<D:
        deal.append(deal_sum[i]/D)
    else:
        deal.append((deal_sum[i]-deal_sum[i-D])/D)
    deal_sum.append(deal[-1]+deal_sum[-1])
#[L,L+D)でディーラーの最終的な値
for i in range(L,L+D+1):
    if i-D>=0:
        deal.append((deal_sum[L]-deal_sum[i-D])/D)
    else:
        deal.append(deal_sum[L]/D)
for i in range(L):
    deal[i] = 0
deal_sum=[deal[0]]
for i in range(1,L+D+1):
    deal_sum.append(deal_sum[-1]+deal[i])
#値iで勝てるのはディーラーの値がi未満またはN以上の時。
#ディーラーの値はL以上L+D-1以下
#print(deal)
if L+D<N+1:
    burst = 0
else:
    burst = 1-deal_sum[N]
val = [0 for i in range(N+D+1)]
for i in range(1,N+D+1):
    if i>N:
        val[i] = 0
        continue
    if i>=L+D:
        val[i] = 1
        continue
    val[i] = burst+deal_sum[i-1]
val[0] = burst
#print(val)
#後ろD個の勝率の平均とそのまま終わった時の勝率のうち、高い方が勝率になる
ans = [0 for i in range(N+D+1)]
check = 0
for i in reversed(range(N+1)):
    ans[i] = max(check/D,val[i])
    check+=ans[i]-ans[i+D]
#print(ans)
print(ans[0])