N, M, L = map(int,input().split())
ans = [0 for i in range(N + 1)]
ans[0] = 1
mod = 998244353
def plus(t):
    global ans
    new_ans = []
    for i in range(N + 1):
        if i < t:
            new_ans.append(ans[i])
        else:
            new_ans.append((ans[i] + new_ans[i - t]) % mod)
    ans = new_ans
def minus(t):
    global ans
    new_ans = []
    for i in range(N + 1):
        if i < t:
            new_ans.append(ans[i])
        else:
            new_ans.append((ans[i] - ans[i - t]) % mod)
    ans = new_ans
for i in range(1,L + 1):
    plus(i)
print(ans[N])
for i in range(1,M - L + 1):
    minus(i)
    plus(i + L)
    print(ans[N])