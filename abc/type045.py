N,K = map(int,input().split())
points = [tuple(map(int,input().split())) for i in range(N)]
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
            if dist_max<(points[bj][0]-points[bi][0])**2+(points[bj][1]-points[bi][1])**2:
                dist_max=(points[bj][0]-points[bi][0])**2+(points[bj][1]-points[bi][1])**2
    subset_score.append(dist_max)
    #bitsで表される部分集合をk個に分割した時の最大値の最小値
from copy import copy
#########################部分集合の部分集合列挙
ans=copy(subset_score)
sub_subset = []
for lb in range(1<<N):
    sss = []
    u = lb
    while u:
        sss.append(u)
        u = (u-1)&lb
    sub_subset.append(sss)
############################################################

for k in range(1,K):
    for lb in reversed(range(1<<N)):
        for sb in sub_subset[lb]:
            if ans[lb-sb]>subset_score[sb]:
                if ans[lb]>ans[lb-sb]:
                    ans[lb]=ans[lb-sb]
            else:
                if ans[lb]>subset_score[sb]:
                    ans[lb]=subset_score[sb]
#for i in range(1<<N):
#    print(ans[i])
print(ans[-1])