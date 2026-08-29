N,K = map(int,input().split())
C = list(map(int,input().split()))
P = list(map(int,input().split()))
#転倒の塊
chunk_sum = []
for i in range(N-1):
    if P[i]>P[i+1]:
        chunk_sum.append(i)
chunk_sum.append(N)
chunk = [chunk_sum[i+1]-chunk_sum[i] for i in range(len(chunk_sum)-1)]
if len(chunk)>K:
    print(-1)
print(chunk)
#普通にdpとしてムズイ
for i in range(K-len(chunk)):
    chunk.append(0)
