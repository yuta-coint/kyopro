N,M = map(int,input().split())
points = [tuple(map(int,input().split())) for i in range(M)]
grid = [[0 for i in range(N)] for j in range(N)]
up = [[-1 for i in range(N)] for j in range(N)]
right = [[-1 for i in range(N)] for j in range(N)]
left = [[-1 for i in range(N)] for j in range(N)]
down = [[-1 for i in range(N)] for j in range(N)]
up_right = [[-1 for i in range(N)] for j in range(N)]
down_right = [[-1 for i in range(N)] for j in range(N)]
up_left = [[-1 for i in range(N)] for j in range(N)]
down_left = [[-1 for i in range(N)] for j in range(N)]
ans = []
vert = [[0 for i in range(N)] for j in range(N)]
hori = [[0 for i in range(N)] for j in range(N)]
minus = [[0 for i in range(2*N+1)] for j in range(2*N+1)]
plus = [[0 for i in range(2*N+1)] for j in range(2*N+1)]
for t in points:
    grid[t[0]][t[1]]=1
c = (N-1)//2
po = []
for i in range(N):
    for j in range(N):
        po.append(((i-c)*(i-c)+(j-c)*(j-c),i,j))
po.sort(reverse=True)
for time in range(50):
    temp=[]
    for i in range(N):
        for j in range(N):
            for k in range(i+1,N):
                if grid[k][j]==1:
                    right[i][j]=k
                    break
            for k in reversed(range(i)):
                if grid[k][j]==1:
                    left[i][j]=k
                    break
            for k in range(j+1,N):
                if grid[i][k]==1:
                    up[i][j]=k
                    break
            for k in reversed(range(j)):
                if grid[i][k]==1:
                    down[i][j]=k
                    break
            for k in range(1,N):
                if i+k>=N or j+k>=N:
                    break
                if grid[i+k][j+k]==1:
                    up_right[i][j]=k
                    break
            for k in range(1,N):
                if i+k>=N or j-k<0:
                    break
                if grid[i+k][j-k]==1:
                    down_right[i][j]=k
                    break
            for k in range(1,N):
                if i-k<0 or j+k>=N:
                    break
                if grid[i-k][j+k]==1:
                    up_left[i][j]=k
                    break
            for k in range(1,N):
                if i-k<0 or j-k<0:
                    break
                if grid[i-k][j-k]==1:
                    down_left[i][j]=k
                    break
    for i in range(N*N):
        p,r=po[i][1],po[i][2]
        if grid[p][r]==1:
            continue
        #if p==8 and r==11:
        #    print(deg,p,r)
        #    print(right[p][r],up[p][r])
        #    print(up[right[p][r]][r],right[p][up[p][r]])
        flag = 0
        q = -1
        s = -1
        if right[p][r]!=-1 and up[p][r]!=-1:
            q = right[p][r]
            s = up[p][r]
            if s==up[q][r] and right[p][s]==q:
                flag=1
        if flag==0:
            if right[p][r]!=-1 and down[p][r]!=-1:
                q = right[p][r]
                s = down[p][r]
                if s==down[q][r] and right[p][s]==q:
                    flag=1
        if flag==0:
            if left[p][r]!=-1 and down[p][r]!=-1:
                q = left[p][r]
                s = down[p][r]
                if s==down[q][r] and q==left[p][s]:
                    flag=1
        if flag==0:
            if left[p][r]!=-1 and up[p][r]!=-1:
                q = left[p][r]
                s = up[p][r]
                if up[q][r]==s and q==left[p][s]:
                    flag=1
        if flag==1:
            min_pq,max_pq = min(p,q),max(p,q)
            min_rs,max_rs = min(r,s),max(r,s)
            for pq in range(min_pq,max_pq+1):
                if hori[pq][r]==1 or hori[pq][s]==1:
                    flag=0
            for rs in range(min_rs,max_rs+1):
                if vert[p][rs]==1 or vert[q][rs]==1:
                    flag=0
        if flag==1:
            for pq in range(min_pq,max_pq+1):
                hori[pq][r]=1
                hori[pq][s]=1
            for rs in range(min_rs,max_rs+1):
                vert[p][rs]=1
                vert[q][rs]=1
            plus[p+r][p-r+N]=1
            minus[p+r][p-r+N]=1
            temp.append((p,r,p,s,q,s,q,r))
            grid[p][r]=1
        if flag==0:
            ur = up_right[p][r]
            ul = up_left[p][r]
            if up_right[p][r]!=-1 and up_left[p][r]!=-1:
                p1,p2,p3,r1,r2,r3 = p+ur,p+ur-ul,p-ul,r+ur,r+ur+ul,r+ul
                if up_right[p3][r3]==ur and up_left[p1][r1]==ul:
                    flag=2
        if flag==0:
            ul = -down_right[p][r]
            ur = -down_left[p][r]
            if down_right[p][r]!=-1 and down_left[p][r]!=-1:
                p1,p2,p3,r1,r2,r3 = p+ur,p+ur-ul,p-ul,r+ur,r+ur+ul,r+ul
                if down_left[p3][r3]==-ur and down_right[p1][r1]==-ul:
                    flag=2
        if flag==0:
            ul = -down_right[p][r]
            ur = up_right[p][r]
            if down_right[p][r]!=-1 and up_right[p][r]!=-1:
                p1,p2,p3,r1,r2,r3 = p+ur,p+ur-ul,p-ul,r+ur,r+ur+ul,r+ul
                if up_right[p3][r3]==ur and down_right[p1][r1]==-ul:
                    flag=2
        if flag==0:
            ul = up_left[p][r]
            ur = -down_left[p][r]
            if up_left[p][r]!=-1 and down_left[p][r]!=-1:
                p1,p2,p3,r1,r2,r3 = p+ur,p+ur-ul,p-ul,r+ur,r+ur+ul,r+ul
                if down_left[p3][r3]==-ur and up_left[p1][r1]==-ul:
                    flag=2
        if flag==2:
            min_sum,max_sum = min(p+r,p1+r1,p2+r2,p3+r3),max(p+r,p1+r1,p2+r2,p3+r3)
            min_diff,max_diff = min(p-r,p1-r1,p2-r2,p3-r3),max(p-r,p1-r1,p2-r2,p3-r3)
            for su in range(min_sum,max_sum+1):
                if plus[su][p-r+N]==1 or plus[su][p2-r2+N]==1:
                    flag=0
            for di in range(min_diff+N,max_diff+N+1):
                if minus[p+r][di]==1 or minus[p+r][di]==1:
                    flag=0
        if flag==2:
            for su in range(min_sum,max_sum+1):
                plus[su][p-r+N]=1
                plus[su][p2-r2+N]=1
            for di in range(min_diff+N,max_diff+N+1):
                minus[p+r][di]=1
                minus[p2+r2][di]=1
            hori[p][r]=1
            vert[p][r]=1
            temp.append((p,r,p1,r1,p2,r2,p3,r3))
            grid[p][r]=1
    ans += temp
print(len(ans))
for i in ans:
    print(*i)