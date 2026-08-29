N =  int(input())
A = list(map(int,input().split()))
q = int(input())
queries =  [list(map(int,input().split())) for i in range(q)]
ls = [(queries[i][0]-1,i) for i in range(q)]
ls.sort()
ls.append((N+2,N))
rs = [(queries[i][1],i) for i in range(q)]
rs.sort()
rs.append((N+2,N))
xs = [queries[i][2] for i in range(q)]
cnt = {xs[i]:0 for i in range(q)}
ansl = [None for i in range(q)]
ansr = [None for i in range(q)]
lc = 0
rc = 0
while ls[lc][0]<1:
    ansl[ls[lc][1]]=cnt[xs[ls[lc][1]]]
    lc+=1
while rs[lc][0]<1:
    ansr[rs[rc][1]]=cnt[xs[rs[rc][1]]]
    rc+=1
for i in range(N):
    if A[i] in cnt:
        cnt[A[i]]+=1
    while ls[lc][0]<i+2:
        ansl[ls[lc][1]]=cnt[xs[ls[lc][1]]]
        lc+=1
    while rs[rc][0]<i+2:
        ansr[rs[rc][1]]=cnt[xs[rs[rc][1]]]
        rc+=1
#print(lc)
#print(rc)
#print(ansr)
#print(ansl)
for i in range(q):
    print(ansr[i]-ansl[i])
