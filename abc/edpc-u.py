N = int(input())
a = [list(map(int,input().split())) for i in range(N)]
#各部分集合について最大値を求める
subset_score = []
for bits in range(1<<N):
    dist_max = 0
    for bi in range(N):
        if (bits>>bi)&1==0:
            continue
        for bj in range(bi+1,N):
            if (bits>>bj)&1==0:
                continue
            dist_max+=a[bi][bj]
    subset_score.append(dist_max)
ans=[0 for i in range(1<<N)]
sub_subset = []
for lb in range(1<<N):
    sss = []
    u = lb
    while u:
        sss.append(u)
        u = (u-1)&lb
    sub_subset.append(sss)

for lb in range(1<<N):
    for sb in sub_subset[lb]:
        if ans[lb]<subset_score[sb]+ans[lb-sb]:
            ans[lb] = subset_score[sb]+ans[lb-sb]
#for i in range(1<<N):
#    print(ans[i])
print(ans[-1])