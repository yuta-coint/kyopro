def Alien(c,XYZ):
    #ここでmax(f(x)-cx)を高速に計算する。さらに、minとなるようなxも調べる
    odd_even = [-10**16 for i in range(8)]
    penalty_count = [0 for i in range(8)]
    odd_even[0] = 0
    for xyz in XYZ:
        new_odd_even = odd_even[:]
        new_penalty_count = penalty_count[:]
        for i in range(3):
            cost = xyz[i]
            for j in range(8):
                if new_odd_even[j] < odd_even[j ^ (1 << i)] + cost - c:
                    new_odd_even[j] = odd_even[j ^ (1 << i)] + cost - c
                    new_penalty_count[j] = penalty_count[j ^ (1 << i)] + 1
                elif new_odd_even[j] == odd_even[j ^ (1 << i)] + cost - c:
                    new_penalty_count[j] = max(new_penalty_count[j], penalty_count[j ^ (1 << i)] + 1)
        odd_even = new_odd_even
        penalty_count = new_penalty_count
    return odd_even[0], penalty_count[0]

def binary_search(K, cakes):
    c_ok = 0
    c_ng = 10**15
    while c_ng - c_ok > 1:
        c_mid = (c_ok + c_ng) // 2
        f, penalty_count = Alien(c_mid, cakes)
        if penalty_count >= 2 * K:
            c_ok = c_mid
        else:
            c_ng = c_mid
        #print(c_ok, c_ng, f, penalty_count)
    ans_c, penalty_count = Alien(c_ok, cakes)
    return ans_c + 2*K * c_ok

T = int(input())
for _ in range(T):
    N, K = map(int,input().split())
    cakes = []
    for i in range(N):
        XYZ = tuple(map(int,input().split()))
        XYZ = tuple(x * 2 for x in XYZ)
        cakes.append(XYZ)
    ans = binary_search(K, cakes)
    print(ans//2)