T = int(input())
import sys
input = sys.stdin.readline
for _ in range(T):
    B,K,Sx,Sy,Gx,Gy = map(int,input().split())
    #K=1,B=1はこの一行で終わり
    ans = (abs(Sx-Gx)+abs(Sy-Gy))*K
    candS = [(Sx-Sx%B,Sy,Sx%B),(Sx+(-Sx)%B,Sy,(-Sx)%B),(Sx,Sy-Sy%B,Sy%B),(Sx,Sy+(-Sy)%B,(-Sy)%B)]
    candG = [(Gx-Gx%B,Gy,Gx%B),(Gx+(-Gx)%B,Gy,(-Gx)%B),(Gx,Gy-Gy%B,Gy%B),(Gx,Gy+(-Gy)%B,(-Gy)%B)]
    #print(ans)
    #print(candS)
    #print(candG)
    for i in candS:
        for j in candG:
            temp = (i[2] + j[2])*K
            if i[0]//B == j[0]//B and i[1]//B == j[1]//B:
                temp+=abs(i[0]-j[0])+abs(i[1]-j[1])
            elif i[0]//B == j[0]//B:
                temp+=abs(i[1]-j[1])
                temp+=min(i[0]%B+j[0]%B,2*B-i[0]%B-j[0]%B)
            elif  i[1]//B == j[1]//B:
                temp+=abs(i[0]-j[0])
                temp+=min(i[1]%B+j[1]%B,2*B-i[1]%B-j[1]%B)
            else:
                temp+=abs(i[0]-j[0])+abs(i[1]-j[1])
            ans = min(ans,temp)
    print(ans)