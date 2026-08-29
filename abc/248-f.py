from copy import copy
N, P= map(int,input().split())
sp = [0 for i in range(3*N+3)]
con  = [0 for i in range(3*N+3)]
up = [0 for i in range(3*N+3)]
ans=[0 for i in range(3*N+3)]
sp[2]+=1
con[3]+=1
up[2]+=1
for _ in range(N-2):
    newsp = [0 for i in range(3*N+3)]
    newcon  = [0 for i in range(3*N+3)]
    newup = [0 for i in range(3*N+3)]
    for i in range(3*N):
        newsp[i+2]+=sp[i]+up[i]*2
        newsp[i+2]%=P
        newcon[i+3]+=sp[i]+con[i]+up[i]*2
        newcon[i+3]%=P
        newcon[i+2]+=con[i]
        newcon[i+2]%=P
        newup[i+2]+=sp[i]+con[i]+up[i]*2
        newup[i+2]%=P
        newup[i+1]+=con[i]
        newup[i+1]%=P
    #print(newsp)
    #print(newcon)
    #print(newup)
    #print(_)
    up = copy(newup)
    con = copy(newcon)
    sp = copy(newsp)
for i in range(3*N+2):
    ans[i+1]+=sp[i]+con[i]+up[i]*2
    ans[i+1]%=P
    ans[i]+=con[i]
    ans[i]%=P
#print(ans)
ans = ans[2*N-1:3*N-2]
ans.reverse()
print(*ans)