import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    C=  list(map(int,input().split()))
    ans = []
    ans_rev = []
    cnt = [0 for i in range(N+1)]
    for i in C:
        cnt[i]+=1
    one = []
    num_one = 0
    for i in range(N+1):
        if cnt[i]==1:
            one.append(i)
            num_one+=1
    if num_one>0:
        num_one-=1
        ans.append(one[num_one])
    for i in range(N+1):
        if cnt[i]<=1:
            continue
        ans.append(i)
        ans_rev.append(i)
        for t in range(cnt[i]-2):
            if num_one>0:
                num_one-=1
                ans.append(one[num_one])
            ans.append(i)
    for i in range(num_one):
        ans.append(one[i])
    ans_rev.reverse()
    print(*(ans+ans_rev))


