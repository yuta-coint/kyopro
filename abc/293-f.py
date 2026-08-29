T = int(input())
for case in range(T):
    N = int(input())
    ans = 0
    for b in range(2,1001):
        n = N
        while n>0:
            if n%b>1:
                break
            n//=b
        else:
            ans+=1
    #1けた
    if N>1000:
        ans+=1
    #2けた
    if N>1001:
        ans+=1
    #3から6桁のケースを個別撃破
    for bits in range(4,64):
        #ok…N以上にするには最低何進法にする必要があるのか
        ok = 10**9
        ng = 1
        while ng+1<ok:
            temp = (ok+ng)//2
            check = 0
            for k in range(6):
                if (bits>>k)&1:
                    check+=temp**k
            if check>=N:
                ok = temp
            else:
                ng = temp
        if ok<1001:
            continue
        check = 0
        for k in range(6):
            if (bits>>k)&1:
                check+=ok**k
        if check == N:
            ans+=1
    print(ans)