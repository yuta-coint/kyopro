#include <iostream>
#include <vector>
#include <algorithm>
#include <atcoder/convolution>
#include <atcoder/modint>

using namespace std;
using namespace atcoder;

// Pythonコードと同じ mod 998244353 を使用
using mint = modint998244353;

/**
 * @brief 形式的冪級数の逆元を求める (Newton法)
 * G_{k+1} = G_k (2 - F * G_k) mod x^(2L)
 * * @param a 元の多項式の係数 F(x)
 * @param deg 求める次数 (mod x^deg)
 * @return vector<mint> 逆元の係数 G(x)
 */
vector<mint> inv_fps(const vector<mint>& a, int deg) {
    if (a.empty() || a[0].val() == 0) {
        // 定数項が0の場合は逆元が存在しない（必要に応じて例外処理）
        return {};
    }

    // 初期値: G_0 = 1 / F(0)
    vector<mint> g = {a[0].inv()};

    // サイズが deg になるまで倍々にしていく
    int m = 1;
    while (m < deg) {
        // 次のステップの次数 (2倍にするが、degを超えないようにする)
        int next_m = min(2 * m, deg);

        // F(x) から必要な次数分だけ取り出す
        vector<mint> f(next_m);
        for (int i = 0; i < next_m; ++i) {
            if (i < (int)a.size()) f[i] = a[i];
            else f[i] = 0;
        }

        // 1. h = F * G_k (mod x^next_m)
        // convolution は NTT を使って高速に乗算を行う
        vector<mint> h = convolution(f, g);
        
        // mod x^next_m なのでサイズを切り詰める
        h.resize(next_m);

        // 2. Compute (2 - h)
        // h[0] = 2 - h[0], h[i] = -h[i] (for i > 0)
        for (int i = 0; i < next_m; ++i) {
            h[i] = -h[i];
        }
        h[0] += 2;

        // 3. G_{next} = G_k * (2 - F * G_k)
        vector<mint> next_g = convolution(g, h);
        
        // 必要な次数まで切り詰める
        next_g.resize(next_m);

        g = next_g;
        m = next_m;
    }

    return g;
}

int main() {
    // 高速I/O
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    if (!(cin >> n)) return 0;

    vector<mint> a(n + 1);
    mint temp = 1;
    for (int i = 0; i < n + 1; ++i) {
        a[i] = temp;
        temp *= (1 + mint(i));
    }

    // 逆元計算
    vector<mint> b = inv_fps(a, n + 1);

    // 出力
    cout << (-b[n]).val() << "\n";

    return 0;
}