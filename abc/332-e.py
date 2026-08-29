N,D = map(int,input().split())
W = list(map(int,input().split()))
ave = sum(W)
#各部分集合について重さの合計を求める
#平均の二乗-二乗の平均が分散
weight_sum = []
for bits in range(1<<N):
    weight = 0
    for bi in range(N):
        if (bits>>bi)&1:
            weight += W[bi]
    weight_sum.append(weight**2)
ans=[10**24 for i in range(1<<N)]
ans[0]=0
for cnt in range(D):
    for lb in reversed(range(1,1<<N)):
        sb = lb
        temp = 10**24
        while sb>lb-sb:
            if temp > weight_sum[sb]+ans[lb-sb]:
                temp = weight_sum[sb]+ans[lb-sb]
            sb = (sb-1)&lb
        ans[lb] = temp
    #print(ans)
#print(ans[-1],ave)
#for i in range(1<<N):
#    print(ans[i])
print((ans[-1]*D-ave**2)/(D*D))