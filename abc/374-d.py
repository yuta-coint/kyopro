import math,itertools
def d(s,t):
    return math.sqrt(((s[1]-t[1])**2+(s[0]-t[00])**2))
N,S,T = map(int,input().split())
senbun = [tuple(map(int,input().split())) for i in range(N)]
ans = 10**24
for p in itertools.permutations(range(N),N):
    for bits in range(1<<N):
        now = (0,0)
        cnt = 0
        for i in range(N):
            if (bits>>i)&1:
                next = (senbun[p[i]][0],senbun[p[i]][1])
            else:
                next = (senbun[p[i]][2],senbun[p[i]][3])
            cnt += d(now,next)/S
            now = next
            if (bits>>i)&1:
                next = (senbun[p[i]][2],senbun[p[i]][3])
            else:
                next = (senbun[p[i]][0],senbun[p[i]][1])
            cnt += d(now,next)/T
            now = next
        if ans>cnt:
            ans = cnt
print(ans)