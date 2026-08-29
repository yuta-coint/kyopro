from itertools import combinations_with_replacement
N,M,Q= map(int,input().split())
q = [tuple(map(int,input().split())) for i in range(Q)]
#M個の列の中からN個の部分列を全探索する
ans = 0
for A in combinations_with_replacement(range(1,M+1),N):
    temp = 0
    for a,b,c,d in q:
        if A[b-1]-A[a-1]==c:
            temp+=d
    if ans<temp:
        ans = temp
print(ans)