import sys
input = sys.stdin.readline
H,W,N,h,w = map(int,input().split())
A = [list(map(int,input().split())) for i in range(H)]
h_max=[-1 for i in range(N+1)]
h_min=[500 for i in range(N+1)]
w_max=[-1 for i in range(N+1)]
w_min=[500 for i in range(N+1)]
for i in range(1,H+1):
    for j in range(1,W+1):
        c=A[i-1][j-1]
        if h_max[c]<i:
            h_max[c]=i
        if w_max[c]<j:
            w_max[c]=j
        if h_min[c]>i:
            h_min[c]=i
        if w_min[c]>j:
            w_min[c]=j
all_color = 0
#何色殺せるか
for k in range(H-h+1):
    all_color = 0
    pre_sum = [0 for l in range(W-w+2)]
    for c in range(1,N+1):
        if h_max==-1:
            continue
        all_color+=1
        if h_max[c]>k+h or h_min[c]<=k:
            continue
        if w_max[c]-w_min[c]>=w:
            continue
        #print(c)
        if 0<=w_min[c]<W-w+1:
            pre_sum[w_min[c]]-=1
        if 0<=w_max[c]-w<W-w+1:
            pre_sum[w_max[c]-w]+=1
        else:
            pre_sum[0]+=1
    #print(pre_sum)
    for l in range(1,W-w+1):
        pre_sum[l]+=pre_sum[l-1]
    #print(pre_sum)
    for l in range(W-w+1):
        pre_sum[l]=all_color - pre_sum[l]
    print(*pre_sum[:W-w+1])