N = int(input())
S = input()
p = ord("a")
ans = 0
for j in range(26):
    alp = chr(p+j)
    last = "0"
    cnt = 0
    ma = 0
    for i in range(N):
        if S[i]==alp:
            cnt+=1
            if cnt>ma:
                ma = cnt
        else:
            cnt = 0
    ans += ma
print(ans)