T = int(input())
for _ in range(T):
    N = int(input())
    S = list(input())
#前から見て行って、i文字目とi+1文字目が違う部分があれば切り替えたい。
    l = N-1
    for i in range(N-1):
        if S[i]>S[i+1]:
            l = i
            break
    r = N
    for i in range(l+1,N):
        if S[l]<S[i]:
            r = i
            break
    print(*(S[:l]+S[l+1:r]+S[l:l+1]+S[r:]),sep="")