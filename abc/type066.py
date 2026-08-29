N = int(input())
ans = 0
ranges = []
for i in range(N):
    L,R = map(int,input().split())
    #それぞれ転倒している確率を調べるxより大きくなる確率
    temp = 0
    for x in range(L,R+1):
        for l,r in ranges:
            if l>x:
                temp+=1
            elif x>=r:
                continue
            else:
                temp += (r-x)/(r-l+1)
        #print(temp)
    temp/=R-L+1
    ans+=temp
    ranges.append((L,R))
print(ans)
