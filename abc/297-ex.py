N = int(input())
cnt = [1,1]
cnt_sum = [1,2]
even_odd_sum = [1,1]
mod = 998244353
#嘘。もっと先まで交代和を取らなきゃいけない
for i in range(2,N+1):
    cnt.append((cnt_sum[i-1]-even_odd_sum[i-2])%mod)
    cnt_sum.append((cnt_sum[-1]+cnt[-1])%mod)
    even_odd_sum.append((even_odd_sum[i-2]+cnt[-1])%mod)
print(cnt)
print(cnt_sum)
print(even_odd_sum)
ans = [0,1]
ans_sum = [0,1]
ans_eo = [0,1]
for i in range(2,N+1):
    ans.append((ans_sum[i-1]-ans_eo[i-2]+cnt_sum[i-1]-2*even_odd_sum[i-2])%mod)
    ans_sum.append((ans_sum[-1]+ans[-1])%mod)
    ans_eo.append((ans_eo[i-2]+ans[-1])%mod)
print(ans[-1])