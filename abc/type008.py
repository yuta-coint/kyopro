n = int(input())
s = input()
mod=10**9+7
ans = [0 for i in range(8)]
atcoder = "atcoder"
ac = {atcoder[i]:i for i in range(7)}
ans[0]=1
for i in range(n):
    if s[i] in ac:
        ans[ac[s[i]]+1] += ans[ac[s[i]]]
        ans[ac[s[i]]+1]%=mod
print(ans[7])