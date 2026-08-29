N,M = map(int,input().split())
#0の個数と1の個数を考えると
number_of_one = [[] for i in range(N+1)]
mod = 998244353
for i in range(N+1):
    for j in range(N+1):
        number_of_one[i].append(pow(2*i*j,M,mod))
    