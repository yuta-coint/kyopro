mod = 998244353
fac = [0 for i in range(10**7)]
fac[0] = 1
for i in range(1, 10**7):
    fac[i] = i * fac[i - 1] %mod
fac_rev = [0] * (10**7)
fac_rev[-1] = pow(fac[-1], -1, mod)
for i in reversed(range(1, 10**7)):
    fac_rev[i - 1] = fac_rev[i] * i %mod
def tree_dp_subtree_size_non_recursive(N, edges, root=0):
    """
    N: 頂点数
    edges: edges[u] は頂点uに隣接する頂点のリスト
    root: 木の根とする頂点番号 (0-indexed)
    """
    parent = [-1] * N
    order = []      # 親から子への順序を記録するリスト
    stack = [root]
    
    # 1. 根から葉へのトポロジカル順序（行きがけ順）を取得する
    while stack:
        u = stack.pop()
        order.append(u)
        for v in edges[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            stack.append(v)
            
    # 各頂点の部分木のサイズを1で初期化
    subtree_size = [1] * N
    
    # 2. 葉から根へ向かって（帰りがけ順で）計算結果を集約する
    for u in reversed(order):
        p = parent[u]
        if p != -1:
            subtree_size[p] += subtree_size[u]
            
    return subtree_size

def tree_dp(N, edges, root=0):
    """
    N: 頂点数
    edges: edges[u] は頂点uに隣接する頂点のリスト
    root: 木の根とする頂点番号 (0-indexed)
    """
    parent = [-1] * N
    order = []      # 親から子への順序を記録するリスト
    stack = [root]
    
    # 1. 根から葉へのトポロジカル順序（行きがけ順）を取得する
    while stack:
        u = stack.pop()
        order.append(u)
        for v in edges[u]:
            if v == parent[u]:
                continue
            parent[v] = u
            stack.append(v)
            
    # 各頂点の部分木のサイズを1で初期化
    subtree_size = [0] * N
    
    # 2. 葉から根へ向かって（帰りがけ順で）計算結果を集約する
    ans = [[] for u in range(N)]
    ans_check = [0 for u in range(N)]
    for u in reversed(order):
        subtree_size[u] += 1
        new_ans_u = [0 for i in range(subtree_size[u])]
        for i in reversed(range(subtree_size[u] - 1)):
            new_ans_u[i] = new_ans_u[i + 1] + ans[u][i] % mod
            new_ans_u[i] %= mod
        if subtree_size[u] == 1:
            new_ans_u[0] = 1
        ans[u] = new_ans_u
        if u == root:
            continue
        p = parent[u]
        ans[u].reverse()
        #print(u,ans[u])
        if ans_check[p] == 0:
            ans_check[p] = 1
            new_ans = ans[u]
        else:
            new_ans = [0 for i in range(subtree_size[p] + subtree_size[u])]
            ans_sum_u = [0 for i in range(subtree_size[u] + 1)]
            ans_sum_p = [0 for i in range(subtree_size[p] + 1)]
            for i in reversed(range(subtree_size[u])):
                ans_sum_u[i] = (ans_sum_u[i + 1] + ans[u][i]) % mod
            for i in reversed(range(subtree_size[p])):
                ans_sum_p[i] = (ans_sum_p[i + 1] + ans[p][i]) % mod
            for i in range(subtree_size[p] + subtree_size[u]):
                start = 0
                if i - subtree_size[u] >= 0:
                    start = i - subtree_size[u]
                for k in range(start,subtree_size[p]):
                    if i < k:
                        break
                    new_ans[i] += ans[p][k] * ans_sum_u[i - k] % mod * fac[i] % mod * fac[subtree_size[p] + subtree_size[u] - i - 1] % mod * fac_rev[k] % mod * fac_rev[i - k] % mod * fac_rev[subtree_size[p] - k - 1] % mod * fac_rev[subtree_size[u] + k - i] % mod
                    new_ans[i] %= mod
            for i in range(subtree_size[p] + subtree_size[u]):
                start = 0
                if i - subtree_size[p] >= 0:
                    start = i - subtree_size[p]
                for k in range(start, subtree_size[u]):
                    if i < k:
                        break
                    new_ans[i] += ans[u][k] * ans_sum_p[i - k] % mod * fac[i] % mod * fac[subtree_size[p] + subtree_size[u] - i - 1] % mod * fac_rev[k] % mod * fac_rev[i - k] % mod * fac_rev[subtree_size[u] - k - 1] % mod * fac_rev[subtree_size[p] + k - i] % mod
                    new_ans[i] %= mod
        ans[p] = new_ans
        #print(ans[p])
        if p != -1:
            subtree_size[p] += subtree_size[u]
    return sum(ans[0])%mod

N = int(input())
G = [set() for i in range(N)]
for i in range(N - 1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    G[a].add(b)
    G[b].add(a)
print(tree_dp(N, G)*2%mod)