N = int(input())
P = list(map(int,input().split()))
S = list(input())
mod = 998244353
end = [False for i in range(N)]
l = 1
for i in range(N):
    end[P[i]-1]=True
    if S[P[i]-1]=="L":
        continue
    elif S[P[i]-1]=="R":
        if end[P[i]%N]:
            continue
        else:
            l=0
    else:
        if end[P[i]%N]:
            l*=2
            l%=mod
        else:
            continue
end = [False for i in range(N)]
r=1
for i in range(N):
    end[P[i]-1]=True
    if S[P[i]-1]=="R":
        continue
    elif S[P[i]-1]=="L":
        if end[(P[i]-2)%N]:
            continue
        else:
            r=0
    else:
        if end[(P[i]-2)%N]:
            r*=2
            r%=mod
        else:
            continue
print((l+r)%mod)