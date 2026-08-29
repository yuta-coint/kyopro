N,K = map(int,input().split())
P = list(map(int,input().split()))
if N == K:
    P.sort()
    print(*P)
    exit()
#ノーダメージ
inc = 0
for i in range(N-1):
    if P[i]<P[i+1]:
        inc+=1
    else:
        inc=0
    if inc>=K-1:
        print(*P)
        exit()
#端以外のルート
temp = 0
for i in reversed(range(1,N-K+1)):
    if P[i-1]>P[i]:
        temp = i
        break
#print(temp)
if min(P[N-K:temp+K])<P[N-K-1]:
    print(*(P[:N-K]+sorted(P[N-K:])))
else:
    print(*(P[:temp]+sorted(P[temp:temp+K])+P[temp+K:]))