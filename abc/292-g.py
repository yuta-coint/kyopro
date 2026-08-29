mod = 998244353
N,M = map(int,input().split())
S = [list(input()) for i in range(N)]
#各区間において、単調増加にできる方法が何通りであるかを計算する。
#dpの実装したくない
ans = [[0 for j in range(N)] for i in range(N)]
for i in reversed(range(M)):
    #[l,r)で単調増加となるi桁目以下の決め方
    new_ans = [[0 for r in range(N+1)] for l in range(N)]
    for l in range(N):
        for r in range(l+1,N+1):
            temp = [0 for _ in range(10)]
            for t in range(l,r):
                if S[i][t]=="?":
                    for b in range(10):