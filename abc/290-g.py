T = int(input())
for case in range(T):
    D,K,X = map(int,input().split())
    #葉の本数を増やす
    ok = 0
    ng = 10**18+1
    while ok+1<ng:
        m = (ok+ng)//2
        cpm=m
        cnt = m
        while cpm>1:
            cpm = ((cpm-1)//K)+1
            cnt+=cpm
        if cnt<=X:
            ok = m
        else:
            ng = m
    #print(ok)
    root = 0
    cpm = ok
    cnt = ok
    for i in range(D):
        cpm = ((cpm-1)//K)+1
        cnt+=cpm
    if cnt<=X:
        root=1
    print((K+1)*X-(X-1)*2-root-ok*K)
