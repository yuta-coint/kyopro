N, K = map(int,input().split())
#和をN,2Nに設定する。
triplets = []
all_same = []
chk = [False for i in range(N)]
if (N*N - K) % 3 == 0:
    for i in range(N):
        for j in range(N):
            k = N-1-(i+j)
            if i > j or i > k:
                continue
            if i == k and j > k:
                continue
            if i == k and j == k:
                all_same.append(i)
                continue
            triplets.append((i,j,k))
    for i in range(N):
        for j in range(N):
            k = 2*N-1-(i+j)
            if k < 0 or k >= N:
                continue
            if i > j or i > k:
                continue
            if i == k and j > k:
                continue
            if i == k and j == k:
                all_same.append(i)
                continue
            triplets.append((i,j,k))
elif (N*N - K)%3 == 1:
    for i in range(N):
        for j in range(N):
            k = N-(i+j)
            if k < 0 or k >= N:
                continue
            if i > j or i > k:
                continue
            if i == k and j > k:
                continue
            if i == k and j == k:
                all_same.append(i)
                continue
            triplets.append((i,j,k))
    for i in range(N):
        for j in range(N):
            k = 2*N-(i+j)
            if k < 0 or k >= N:
                continue
            if i > j or i > k:
                continue
            if i == k and j > k:
                continue
            if i == k and j == k:
                all_same.append(i)
                continue
            triplets.append((i,j,k))
else:
    all_same.append(0)
    for i in range(N):
        for j in range(N):
            k = N-1-(i+j)
            if i == 0 and j == 0:
                continue
            if i > j or i > k:
                continue
            if i == k and j > k:
                continue
            if i == k and j == k:
                all_same.append(i)
                continue
            triplets.append((i,j,k))
    for i in range(N):
        for j in range(N):
            k = 2*N-1-(i+j)
            if k < 0 or k >= N:
                continue
            if i > j or i > k:
                continue
            if i == k and j > k:
                continue
            if i == k and j == k:
                all_same.append(i)
                continue
            triplets.append((i,j,k))
for i in range(len(triplets)):
    if K < 3:
        break
    s,t,u = triplets[i]
    print(s,t,u)
    print(t,u,s)
    print(u,s,t)
    K -= 3
for i in range(K):
    s = all_same[i]
    print(s,s,s)