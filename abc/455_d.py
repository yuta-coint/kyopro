N,Q = map(int,input().split())
CP = [tuple(map(int,input().split())) for i in range(Q)]
son = [-1 for i in range(N)]
mother = [-1 for i in range(N)]
for i in reversed(range(Q)):
    c,p = CP[i]
    c -= 1
    p -= 1
    if son[c] == -1:
        son[c] = p
        mother[p] = c
answers = []
for i in range(N):
    if son[i] == -1:
        ans = 1
        t = i
        while mother[t] != -1:
            t = mother[t]
            ans += 1
    else:
        ans = 0
    answers.append(ans)
print(*answers)