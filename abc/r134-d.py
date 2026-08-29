n = int(input())
a0 = list(map(int,input().split()))
b = sorted(set(a0))
d1 = {v:i for i, v in enumerate(b)}
d2 = {i:v for i, v in enumerate(b)}
a = list(map(lambda v:d1[v],a0))
un = a[:n]
dn = a[n:]
#そこから右の最小値
mi = [un[n-1]]
for i in reversed(range(n-1)):
    mi.append(min(mi[-1],un[i]))
for i in range(n//2):
    mi[i],mi[n-1-i] = mi[n-1-i],mi[i]
mi.append(-1)
cnt = [0 for i in range(2*n)]
for i in range(n):
    cnt[un[i]]+=1
ansl = []
k = mi[0]
kk = -1
t = n-1
for i in range(n):
    cnt[un[i]]-=1
    if un[i]==k:
        if kk==-1:
            kk=dn[i]
        ansl.append(i)
        if cnt[un[i]]==0:
            k = mi[i+1]
            if k==kk:
                t = i
                break
            elif k>kk:
                break
f4 = 0
for i in range(1,len(ansl)):
    if dn[ansl[i]]>kk:
        f4 = 1
        break
    elif dn[ansl[i]]<kk:
        break
if f4==1:
    for i in range(t+1,n):
        if un[i]==k:
            ansl.append(i)
ans = [d2[un[i]] for i in ansl]+[d2[dn[i]] for i in ansl]
ans2 = [mi[0],mi[0]+1]
for i in range(n):
    if un[i]==mi[0]:
        ans2[1]=min(ans2[1],dn[i])
if ans2[0]>=ans2[1]:
    ans = [d2[ans2[0]],d2[ans2[1]]]
print(*ans)