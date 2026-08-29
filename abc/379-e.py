N=  int(input())
S = list(input())
for i in range(N):
    S[i] = int(S[i])
ans = 0
ans = [0 for i in range(N+30)]
mns = 0
for i in range(N):
    temp = (i+1)*S[i]
    mns += (i+1)*S[i]
    cnt = 0
    while temp>0:
        ans[N-i+cnt]+=temp%10
        j=cnt
        while ans[N-i+j]>=10:
            ans[N-i+j]-=10
            ans[N-i+1+j]+=1
            j+=1
        temp//=10
        cnt+=1
cnt = 0
while mns>0:
    ans[cnt]-=mns%10
    j = 0
    while ans[cnt+j]<0:
        ans[cnt+j]+=10
        ans[cnt+j+1]-=1
        j+=1
    cnt+=1
    mns//=10
amari = 0
keta = -1
for i in reversed(range(N+30)):
    ans[i]+=10*amari
    #print(ans[i],amari)
    amari = ans[i]%9
    ans[i]//=9
    if keta==-1 and ans[i]>0:
        keta = i+1
#print(ans)
ans = ans[:keta]
ans.reverse()
print(*ans,sep="")