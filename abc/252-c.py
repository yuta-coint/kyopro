N = int(input())
ans = [0 for i in range(10)]
stop = [[0 for j in range(10)] for i in range(10)]
for i in range (N):
    S = input()
    for j in range(10):
        k = int(S[j])
        stop[k-1][j]+=1
for i in range(10):
    for j in range(10):
        if stop[i][j]==0:
            continue
        else:
            ans[i]=max(ans[i],10*(stop[i][j]-1)+j)
print(min(ans))

