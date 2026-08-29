K = int(input())
Sx,Sy = map(int,input().split())
Tx,Ty = map(int,input().split())
if ((Sx//K)+(Sy//K))&1:
    cands = [(Sx//K,Sy//K,0)]
else:
    cands = [((Sx-K)//K,Sy//K,Sx%K+1),(Sx//K,(Sy-K)//K,Sy%K+1),((Sx+K)//K,Sy//K,(K-Sx%K)),(Sx//K,(Sy+K)//K,(K-Sy%K))]
if ((Tx//K)+(Ty//K))&1:
    candt = [(Tx//K,Ty//K,0)]
else:
    candt = [((Tx-K)//K,Ty//K,Tx%K+1),(Tx//K,(Ty-K)//K,Ty%K+1),((Tx+K)//K,Ty//K,(K-Tx%K)),(Tx//K,(Ty+K)//K,(K-Ty%K))]
#print(cands)
#print(candt)
ans = (abs(Sx-Tx)+abs(Sy-Ty))
for s1,s2,s3 in cands:
    for t1,t2,t3 in candt:
        temp = t3+s3
        temp += abs((s1+s2)-(t1+t2))+abs((s1-s2)-(t1-t2))
        if ans >temp:
            ans = temp
if K==2:  
    for s1,s2,s3 in cands:
        for t1,t2,t3 in candt:
            temp = t3+s3
            ma = abs(s1-t1)
            mi = abs(s2-t2)
            if ma<mi:
                ma,mi = mi,ma
            #print(ma,mi)
            temp += mi*2+((ma-mi)*3//2)
            if ans >temp:
                ans = temp
print(ans)