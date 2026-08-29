import sys
input = sys.stdin.readline
def main():
    N = int(input())
    points = []
    for i in range(N):
        pa,pb = map(int,input().split())
        points.append((pa,pb))
    xs =[points[i][0] for i in range(N)]
    ys =[points[i][1] for i in range(N)]
    def area_try(xa,ya,xb,yb,xc,yc):
        return(abs((xa-xc)*(yb-ya)-(xa-xb)*(yc-ya)))
    #多角形の二倍
    area_all = 0
    for j in range(1,N-1):
        k = (j+1)%N
        area_all += area_try(xs[0],ys[0],xs[j],ys[j],xs[k],ys[k])
    j = 1
    #今見ている領域の8倍
    area_now = 0
    ans = float("inf")
    for i in range(N):
        if area_now<area_all:
            while True:
                #もう一個足したら死ぬとこまで足し続ける。
                k = (j+1)%N
                #######################################
                area_plus = 4*area_try(xs[i],ys[i],xs[j],ys[j],xs[k],ys[k])
                ans = min(abs(area_now+area_plus-area_all),ans)
                if area_now+area_plus>area_all:
                    break
                area_now+=area_plus
                ###################################
                j+=1
                j%=N
        #iを増やすと潰れるならばjを1増やして対応する。
        if j==(i+1)%N:
            ##############
            k = (j+1)%N
            area_now+=4*area_try(xs[i],ys[i],xs[j],ys[j],xs[k],ys[k])
            #################
            j+=1
            j%=N
        #iのスライドを反映
        area_now-=4*area_try(xs[i],ys[i],xs[(i+1)%N],ys[(i+1)%N],xs[j],ys[j])
        ############################################
        ans = min(abs(area_now-area_all),ans)
    print(ans)
main()
