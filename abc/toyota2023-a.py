N,M,V = map(int,input().split())
ans = 0
for H in range(1,N+1):
    for W in range(1,M+1):
        if (V*2)%(H*W)!=0:
            continue
        ave = V*2//(H*W)
        ave-=(H-1)*M
        ave-=(W+1)
        if ave&1 or ave<0:
            continue
        ave//=2
        i = ave//M
        j = ave%M
        if i+H-1>=N:
            continue
        if j+W-1>=M:
            continue
        ans+=1
        #print(i,j,H,W)
print(ans)