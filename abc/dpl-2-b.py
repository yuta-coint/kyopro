#中国人郵便配達問題
v, e = map(int,input().split())
length = [[float('inf') for i in range(v)] for j in range(v)]
cnt = [0 for i in range(v)]
for i in range(v):
    length[i][i]=0
base = 0
for i in range(e):
    a,b,c = map(int,input().split())
    length[a][b] = min(length[a][b],c)
    length[b][a] = min(length[b][a],c)
    base+=c
    cnt[a]+=1
    cnt[b]+=1
for i in range(v):
     for j in range(v):
         for k in range(v):
             if length[j][i]!=float('inf') and length[i][k]!=float('inf'):
                 if length[j][k]>length[j][i]+length[i][k]:
                     length[j][k]=length[j][i]+length[i][k]
ans = [float('inf') for i in range(2**v)]
ans[0]=0
for odd_bit in range(2**v):
    for i in range(v):
        for j in range(i+1,v):
            if odd_bit>>i & odd_bit>>j & 1:
                ans[odd_bit] = min(ans[odd_bit],ans[odd_bit-2**i-2**j]+length[i][j])
odd_node = [(cnt[i]&1)*2**i for i in range(v)]
#print(ans)
#print(odd_node)
print(ans[sum(odd_node)]+base)