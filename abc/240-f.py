from re import S


T = int(input())
for _ in range(T):
    sumb = 0
    sumc = 0
    N,M = map(int,input().split())
    ans = -float("inf")
    for i in range(N):
        x,y = map(int,input().split())
        if i==0:
            ans = x
        if x>=0:
            sumc+=sumb*y
            sumc+=(y*(y+1)*x)//2
            sumb += x*y
            ans = max(ans,sumc)
        else:
            if 0<sumb//(-x)<y:
                y1 = sumb//(-x)
                tempc = sumc+sumb*y1
                tempc += (y1*(y1+1)*x)//2
                ans = max(ans,tempc)
            sumc+=sumb*y
            sumc+=(y*(y+1)*x)//2
            sumb += x*y
            ans = max(ans,sumc)
    print(ans)


