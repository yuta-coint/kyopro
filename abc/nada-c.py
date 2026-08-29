import sys
input = sys.stdin.readline
import queue
def main():
    h,w,n = map(int,input().split())
    bomb = [list(map(int,input().split())) for i in range(n)]
    #奇偶を合わせる
    for i in range(n):
        if (bomb[i][2]+bomb[i][0]+bomb[i][1])&1:
            bomb[i][2]+=1
    labyrinth = [["#" for i in range(w+2)]]
    for i in range(h):
        labyrinth.append(["#"]+list(input())+["#"])
    labyrinth.append(["#" for i in range(w+2)])
    ans = 0
    #(sy,sxからの距離を出力)
    def bfs(sy,sx):
        new = queue.Queue()
        chk = [0 for i in range((h+1)*(w+1)+1)]
        ans = [float('inf') for i in range((h+1)*(w+1)+1)]
        t = (sy,sx,0)
        new.put(t)
        chk[sy+sx*(h+1)]=1
        counter = 0
        while not new.empty():
            point = new.get()
            py = point[0]
            px = point[1]
            counter = point[2]+1
            ans[py+px*(h+1)]=counter-1
            if labyrinth[py-1][px]=="." and chk[py-1+px*(h+1)]==0:
                    new.put([py-1,px,counter])
                    chk[py-1+px*(h+1)]=1
            if labyrinth[py][px-1]=="." and chk[py+(px-1)*(h+1)]==0:
                new.put([py,px-1,counter])
                chk[py+(px-1)*(h+1)]=1
            if labyrinth[py][px+1]=="." and chk[py+(px+1)*(h+1)]==0:
                new.put([py,px+1,counter])
                chk[py+(px+1)*(h+1)]=1
            if labyrinth[py+1][px]=="." and chk[py+1+px*(h+1)]==0:
                new.put([py+1,px,counter])
                chk[py+1+px*(h+1)]=1
        return(ans)
 
    dist = [[0 for i in range(n)] for j in range(n)]
    for i in range(n):
        s = bfs(bomb[i][0],bomb[i][1])
        for j in range(n):
            dist[i][j] = s[bomb[j][0]+bomb[j][1]*(h+1)]
    dp = [[float('inf') for j in range(n)] for i in range(2**n)]
    #iのマスを網羅してjにいる方法
    s1=bfs(1,1)
    for j in range(n):
        dp[2**j][j]=s1[bomb[j][0]+bomb[j][1]*(h+1)]
        if dp[2**j][j]>bomb[j][3]:
            dp[2**j][j]=float('inf')
        else:
            dp[2**j][j]=max(bomb[j][2],dp[2**j][j])
    for i in range(2**n):
        #いまいる場所
        cnt = 0
        dpi = dp[i]
        for j in range(n):
            if (i>>j)&1:
                cnt+=1
                #k:直前にいた場所
                for k in range(n):
                    if (i>>k)&1 and j!=k:
                        dpi[j]=min(dp[i-2**j][k]+dist[j][k],dpi[j])
            #間に合いますか
            if dpi[j]>bomb[j][3] or bomb[j][3]<bomb[j][2]:
                dpi[j]=float('inf')
            else:
                dpi[j] = max(bomb[j][2],dpi[j])
        for j in range(n):
            if dpi[j]!=float('inf'):
                ans = max(ans,cnt)
        dp[i]=dpi
    print(ans)
main()