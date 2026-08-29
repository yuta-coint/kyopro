#include <iostream>
#include <vector>
#include <algorithm>
#include <atcoder/convolution>
#include <atcoder/modint>

using namespace std;
using namespace atcoder;

using mint = modint998244353;

/**
 * @brief 形式的冪級数の逆元を求める (Newton法)
 * G_{k+1} = G_k (2 - F * G_k) mod x^(2L)
 */
vector<mint> inv_fps(const vector<mint>& a, int deg) {
    if (a.empty() || a[0].val() == 0) {
        return {};
    }
    vector<mint> g = {a[0].inv()};
    int m = 1;
    while (m < deg) {
        int next_m = min(2 * m, deg);
        vector<mint> f(next_m);
        for (int i = 0; i < next_m; ++i) {
            if (i < (int)a.size()) f[i] = a[i];
            else f[i] = 0;
        }
        vector<mint> h = convolution(f, g);
        h.resize(next_m);
        for (int i = 0; i < next_m; ++i) h[i] = -h[i];
        h[0] += 2;
        vector<mint> next_g = convolution(g, h);
        next_g.resize(next_m);
        g = next_g;
        m = next_m;
    }
    return g;
}

/**
 * @brief 形式的冪級数の対数を求める
 * log(F) = ∫(F'/F) dx
 */
vector<mint> log_fps(const vector<mint>& a, int deg) {
    if (a.empty() || a[0].val() != 1) return {}; // log(F)はF(0)=1であることを前提とする実装が多い
    
    vector<mint> a_deriv(a.size() - 1);
    for (int i = 1; i < (int)a.size(); ++i){
        a_deriv[i - 1] = a[i] * mint(i);
    }
    
    // inv_fps は次数 deg-1 までで十分だが、convolutionの結果のサイズ調整で合わせる
    vector<mint> a_inv = inv_fps(a, deg - 1); 
    
    vector<mint> q = convolution(a_deriv, a_inv);
    q.resize(deg - 1);
    
    vector<mint> log_a(deg);
    log_a[0] = 0; // log(1) = 0
    for (int i = 1; i < deg; ++i) {
        log_a[i] = q[i - 1] * mint(i).inv(); // / i は * inv(i)
    }
    return log_a;
}

/**
 * @brief 形式的冪級数の指数関数を求める (Newton法)
 * G_{k+1} = G_k (1 - log(G_k) + F) mod x^(2L)
 * 前提: a[0] = 0
 */
vector<mint> exp_fps(const vector<mint>& a, int deg) {
    // 定数項が0でないと exp(f) は形式的冪級数として単純に定義できない
    if (a.empty()) return {1};
    if (a[0].val() != 0) return {}; 

    // 初期値: exp(0) = 1
    vector<mint> g = {1};

    int m = 1;
    while (m < deg) {
        int next_m = min(2 * m, deg);

        // F(x) から必要な次数分だけ取り出す
        vector<mint> f(next_m);
        for (int i = 0; i < next_m; ++i) {
            if (i < (int)a.size()) f[i] = a[i];
            else f[i] = 0;
        }

        // 1. log_g = log(G_k) mod x^next_m
        vector<mint> log_g = log_fps(g, next_m);
        
        // 2. h = 1 - log(G_k) + f
        // f[i] - log_g[i] を計算し、定数項に +1
        vector<mint> h(next_m);
        for (int i = 0; i < next_m; ++i) {
            h[i] = f[i] - log_g[i];
        }
        h[0] += 1;

        // 3. G_{next} = G_k * h
        vector<mint> next_g = convolution(g, h);
        
        // 必要な次数まで切り詰める
        next_g.resize(next_m);

        g = next_g;
        m = next_m;
    }

    return g;
}

int main(){
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    int N;
    if (!(cin >> N)) return 0;
    
    vector<mint> a(N + 1, 0);
    mint mother = 1;
    for (int i = 0; i < N; ++i) {
        mother *= mint(i + 1);
    }
    mother  = mother.inv();
    for(int i=N; i >= 0; --i){
        long p = (long)i * (i - 1) /2;
        mint son = mint(2).pow(p);
        a[i] = son * mother;
        mother *= mint(i);
    }
    cerr << a[0].val() << "\n";
    
    vector<mint> log_a = log_fps(a, N + 1);
    
    mint ans = log_a[N];
    for (int i = 1; i <= N; ++i) {
        ans *= mint(i);
    }

    cout << ans.val() << "\n";
    return 0;
}