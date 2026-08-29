mod = 998244353
N,X = map(int,input().split())
if N<X:
    print(0)
    exit()
cut = [1]
for sq in range(1,N+1):
    #一列目とi行目を抜いた時に何通りあるか
    new_cut = [0 for i in range(sq+1)]
    for i in range(sq+1):
        for j in range(sq+1):
            if 