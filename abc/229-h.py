import sys
def frac_max(p,q):
    if p[0] * q[1] > q[0] * p[1]:
        return p
    else:
        return q
def frac_min(p,q):
    if p[0] * q[1] < q[0] * p[1]:
        return p
    else:
        return q
N = int(input())
Game = [(-1, -1) for i in range(3 ** N)]
for state in range(3 ** N):
    if state == 0:
        Game[0] = (0,1)
        continue
    board = []
    for i in range(N):
        board.append((state // (3 ** i)) % 3)
    max_a = (-10**9, 1)
    ## Aの手番
    for i in range(N):
        if board[i] != 1:
            continue
        next_game = Game[state - (3 ** i)]
        max_a = frac_max(max_a, next_game)
    for i in range(N - 1):
        if board[i] != 0 or board[i + 1] != 2:
            continue
        next_game = Game[state + 2 * (3 ** i) - 2 * (3 ** (i + 1))]
        max_a = frac_max(max_a, next_game)
    ## Bの手番
    min_b = (10**9, 1)
    for i in range(N):
        if board[i] != 2:
            continue
        next_game = Game[state - 2 * (3 ** i)]
        min_b = frac_min(min_b, next_game)
    for i in range(N - 1):
        if board[i] != 0 or board[i + 1] != 1:
            continue
        next_game = Game[state + (3 ** i) -  (3 ** (i + 1))]
        min_b = frac_min(min_b, next_game)
    assert frac_max(max_a, min_b) == min_b
    if max_a[0] < 0 < min_b[0]:
        Game[state] = (0, 1)
        continue
    if min_b[0] <= 0:
        r = 1
        while True:
            s = ((- min_b[0] * r) // min_b[1]) + 1
            if frac_max((-s, r), max_a) == max_a:
                r *= 2
                continue
            else:
                Game[state] = (-s, r)
                break
    else:
        r = 1
        while True:
            s = ((max_a[0] * r) // max_a[1]) + 1
            if frac_min((s, r), min_b) == min_b:
                r *= 2
                continue
            else:
                Game[state] = (s, r)
                break
    print(state,Game[state], file=sys.stderr)
print(Game, file=sys.stderr)
S= [input() for _ in range(N)]
ans = 0
for j in range(N):
    state = 0
    for i in range(N):
        if S[i][j] == "B":
            state += 1 * (3 ** i)
        elif S[i][j] == "W":
            state += 2 * (3 ** i)
    ans += Game[state][0] * (1 << 16) // Game[state][1]
if ans > 0:
    print("Takahashi")
else:
    print("Snuke")