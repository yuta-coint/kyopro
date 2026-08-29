#並び替えて同じになる状況をまとめるタイプのdp
N = int(input())
ans = [[[0 for k in range(1+N-i-j)] for j in range(1+N-i)]for i in range(N+1)]
a = list(map(int,input().split()))
I,J,K = 0,0,0
for i in a:
    if i==1:
        I+=1
    elif i==2:
        J+=1
    else:
        K+=1
for k in range(N+1):
    for j in range(N+1-k):
        for i in range(N+1-k-j):
            if i==j==k==0:
                continue
            temp = 0
            if i>0:
                temp+=i*ans[i-1][j][k]
            if j>0:
                temp+=j*ans[i+1][j-1][k]
            if k>0:
                temp+=k*ans[i][j+1][k-1]
            ans[i][j][k]=(temp+N)/(i+j+k)
print(ans[I][J][K])