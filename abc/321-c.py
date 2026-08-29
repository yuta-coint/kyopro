from itertools import combinations
K = int(input())
for keta in range(1,11):
    #keta桁の321likeのうち、K番目に小さいやつを求める
    for t in reversed(list(combinations(reversed(range(10)),keta))):
        if t[0]==0:
            continue
        K-=1
        if K==0:
            print(*t,sep="")
            exit()
