import math
import random
import time


def solve():
    N = int(input())
    XY = [tuple(map(int, input().split())) for _ in range(N)]

    def dist(i, j):
        xi, yi = XY[i]
        xj, yj = XY[j]
        return math.hypot(xi - xj, yi - yj)

    # -------------------------
    # 距離行列
    # -------------------------
    D = [[0.0] * N for _ in range(N)]

    for i in range(N):
        for j in range(i + 1, N):
            d = dist(i, j)
            D[i][j] = d
            D[j][i] = d

    # -------------------------
    # 初期解
    # -------------------------
    tour = list(range(N))

    # 都市0を先頭に固定しておく
    rest = tour[1:]
    random.shuffle(rest)
    tour = [0] + rest

    def calc_length():
        res = 0.0
        for i in range(N):
            res += D[tour[i]][tour[(i + 1) % N]]
        return res

    current = calc_length()

    best = current
    best_tour = tour[:]

    # -------------------------
    # 焼きなまし
    # -------------------------
    TIME_LIMIT = 1.9

    START_TEMP = 100.0
    END_TEMP = 0.01

    start_time = time.perf_counter()

    iteration = 0
    temp = START_TEMP

    while True:
        iteration += 1

        if iteration & 255 == 0:
            elapsed = time.perf_counter() - start_time

            if elapsed >= TIME_LIMIT:
                break

            progress = elapsed / TIME_LIMIT

            temp = START_TEMP * (END_TEMP / START_TEMP) ** progress

        # --------------------------------
        # 2-opt
        #
        #    a -- b       a    b
        #         |        \  /
        #         |   ->    \/
        #         |         /\
        #    d -- c       d    c
        #
        # [l, r] を反転
        # --------------------------------

        l = random.randrange(1, N - 1)
        r = random.randrange(l + 1, N)

        a = tour[l - 1]
        b = tour[l]

        c = tour[r]
        d = tour[(r + 1) % N]

        # 古い辺
        old_cost = D[a][b] + D[c][d]

        # 新しい辺
        new_cost = D[a][c] + D[b][d]

        # 新 - 旧
        diff = new_cost - old_cost

        # 最小化なので、
        # diff < 0 なら改善
        if diff <= 0 or random.random() < math.exp(-diff / temp):

            # 区間反転
            tour[l:r + 1] = reversed(tour[l:r + 1])

            current += diff

            if current < best:
                best = current
                best_tour = tour[:]

    # -------------------------
    # 出力
    # -------------------------
    for v in best_tour:
        print(v)

    # 最後に都市0へ戻る形式なら
    print(best_tour[0])

    # デバッグ
    # print("length =", best, file=sys.stderr)
    # print("iteration =", iteration, file=sys.stderr)


if __name__ == "__main__":
    solve()