N,M = map(int,input().split())
SS = [input() for i in range(N)]
T = [input() for i in range(M)]
T = set(T)
ans = -1
import itertools
ptn = list(itertools.permutations(SS))
#k:つぎにS[k]を付け足すub個の枠が余裕として残っている
flag = 0
def search(sub,k,ub):
    global ans
    global flag
    if flag == 0:
        if k == N:
            if not (sub in T) and len(sub)>=3:
                ans = sub
                #print(sub,k,ub)
                flag = 1
        else:
            sub+="_"
            for i in range(ub+1):
                search(sub+S[k],k+1,ub-i)
                sub+="_"
ls = 0
for i in range(N):
    ls+=len(SS[i])
#print(ptn)
for p in ptn:
    S = p
    search(S[0],1,16-ls-(N-1))
print(ans)