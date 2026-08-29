N,Q = map(int,input().split())
mod = 10**9+7
xyzw = [tuple(map(int,input().split())) for i in range(Q)]
ans = 1
for b in range(60):
    #全探索する
    cnt = 0
    for bits in range(1<<N):
        #要請にあっているか確認する
        for x,y,z,w in xyzw:
            if ((bits>>(x-1))|(bits>>(y-1))|(bits>>(z-1)))&1!=(w>>b)&1:
                break
        else:
            cnt+=1
    ans*=cnt
    ans%=mod
print(ans)