def floor_sum(n,m,a,b):
    res = 0
    while True:
        if a >= m:
            res += (a//m)*n*(n-1)//2
            a %= m
        if b >= m:
            res += n*(b//m)
            b %= m
        if a*n+b < m:
            break
        u = (a*n+b)//m
        v = u*m-b
        res += (n-(v+a-1)//a)*u
        n,m,a,b = u,a,m,(a-v)%a
    return res
T = int(input())
for case in range(T):
    N,M,R = map(int,input().split())
    if R>N:
        print(0)
        continue
    cnt = 1+(N-R)//M
    ans = (2*R+(cnt-1)*M)*cnt//2
    #print(ans)
    for b in range(1,40):
        ans -= floor_sum(cnt,1<<b,M,R)
    print(ans)
