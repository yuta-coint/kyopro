N,M = map(int,input().split())
intervals = [tuple(map(int,input().split())) for i in range(M)]
itv2=[]
ans = [0 for i in range(M)]
for i in range(M):
    l,r = intervals[i]
    itv2.append(l*(10**15)+(10**7-r)*10**7+i)
    if l== 1 and r==N:
        print(1)
        ans[i]=1
        print(*ans)
        exit()
if M == 1:
    print(-1)
    exit()
#disjointな二つを2,2にする
Lmin = (10**9,-1)
Lmax = (-1,-1)
Rmin = (10**9,-1)
Rmax = (-1,-1)
for i in range(M):
    l,r = intervals[i]
    if l<Lmin[0]:
        Lmin = (l,i)
    if l>Lmax[0]:
        Lmax = (l,i)
    if r<Rmin[0]:
        Rmin = (r,i)
    if r>Rmax[0]:
        Rmax = (r,i)
if Rmin[0]<Lmax[0]:
    print(2)
    ans[Lmax[1]]=2
    ans[Rmin[1]]=2
    print(*ans)
    exit()
if Lmin[0]==1 and Rmax[0]==N:
    print(2)
    ans[Lmin[1]]=1
    ans[Rmax[1]]=1
    print(*ans)
    exit()
#print(1%0)
#一方が一方を包含する場合。
itv2.sort()
Rm = (-1,-1)
for j in range(M):
    ri = itv2[j]%(10**15)
    r = 10**7-(ri//10**7)
    i = ri%10**7
    #print(r,i)
    if r>Rm[0]:
        Rm = (r,i)
    else:
        print(2)
        ans[i] = 2
        ans[Rm[1]] = 1
        print(*ans)
        #print(i,Rm[1])
        exit() 
if M==2:
    print(-1)
    exit()
ans[Lmin[1]]=1
ans[Rmax[1]]=1
for i in range(M):
    if ans[i]==0:
        ans[i]=2
        break
print(3)
print(*ans)