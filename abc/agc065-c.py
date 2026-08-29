T = int(input())
for case in range(T):
    N = int(input())
    A = list(map(int,input().split()))
    #奇数偶数混合アタックはナシとする。
    odd = []
    for i in range(N):
        if A[i]&1:
            odd.append(A[i])
    odd_cnt = len(odd)
    if max(A)>odd_cnt:
        print("Yes")
        continue
    odd.sort(reverse=True)
    ans = "No"
    for i in range(odd_cnt):
        if i&1:
            continue
        if odd[i]>odd_cnt-i-1:
            ans = "Yes"
    print(ans)