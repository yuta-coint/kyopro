#基本的に出てきたキャラを降順に並び替えるのが強い
N,M = map(int,input().split())
S = list(input())
for i in range(N):
    S[i]=int(S[i])
T = list(input())
for i in range(M):
    T[i]=int(T[i])
U = [-10]+sorted(T)
ans = []
cnt = [0 for i in range(10)]
for i in range(N):
    if S[i]<U[-1]:
        ans.append(U.pop())
    else:
        ans.append(S[i])
    cnt[ans[-1]]+=1
#無駄打ちができるかどうか
temp = -1
#ans[-1]以上のやつはできる限り消費を遅らせる。
for i in range(M):
    if cnt[T[i]]>0:
        temp = -1
    else:
        temp = T[i]
if temp!=-1:
    ans[-1]=temp
print(*ans,sep="")