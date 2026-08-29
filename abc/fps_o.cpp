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

vector<mint> pow_fps(vector<mint> a, long long k, int deg) {
    int n = a.size();
    
    // 1. 先頭の0の個数 d を数える
    int d = 0;
    while (d < n && a[d].val() == 0) {
        d++;
    }

    // 係数がすべて0の場合
    if (d == n) {
        if (k == 0) {
            vector<mint> res(deg, 0);
            if (deg > 0) res[0] = 1;
            return res;
        } else {
            return vector<mint>(deg, 0);
        }
    }

    // 2. 結果の次数が deg 以上になる場合 (d * k >= deg)
    // オーバーフローに注意して判定
    if (k > 0 && (long long)d * k >= deg) {
        return vector<mint>(deg, 0);
    }
    
    // k=0 の場合は 1
    if (k == 0) {
        vector<mint> res(deg, 0);
        if (deg > 0) res[0] = 1;
        return res;
    }

    // 3. 正規化: f(x) = x^d * c * h(x)  (h(0)=1)
    // h(x) を取り出す。必要な次数は deg - d*k
    int len = deg - d * k;
    vector<mint> h(len);
    mint c = a[d];
    mint c_inv = c.inv();
    
    for (int i = 0; i < len; ++i) {
        if (d + i < n) h[i] = a[d + i] * c_inv;
        else h[i] = 0;
    }

    // 4. h(x)^k = exp(k * log(h(x))) を計算
    // h(0)=1 なので log, exp が使える
    vector<mint> log_h = log_fps(h, len);
    
    mint mk = k; // k mod 998244353
    for (int i = 0; i < len; ++i) {
        log_h[i] *= mk;
    }
    
    vector<mint> h_pow_k = exp_fps(log_h, len);

    // 5. 復元: x^{dk} * c^k * h(x)^k
    vector<mint> res(deg, 0);
    mint c_pow_k = c.pow(k);
    
    int shift = d * k;
    for (int i = 0; i < len; ++i) {
        res[shift + i] = h_pow_k[i] * c_pow_k;
    }

    return res;
}

// エラトステネスの篩
// n以下の素数のリストを返す
vector<int> sieve_of_eratosthenes(int n) {
    // prime[i] := iが素数ならtrue, そうでなければfalse
    // n+1個の要素をtrueで初期化
    vector<bool> prime(n + 1, true);

    if (n >= 0) prime[0] = false;
    if (n >= 1) prime[1] = false;

    // Pythonの for i in range(2, sqrt_n) に相当
    // C++では i * i <= n と書くのが一般的でバグりにくい
    for (int i = 2; i * i <= n; ++i) {
        if (prime[i]) {
            // Pythonの range(2*i, n+1, i) に相当
            // iの倍数を篩落とす
            for (int j = 2 * i; j <= n; j += i) {
                prime[j] = false;
            }
        }
    }

    // 素数リストの作成
    vector<int> list_of_prime;
    for (int i = 0; i <= n; ++i) {
        if (prime[i]) {
            list_of_prime.push_back(i);
        }
    }

    return list_of_prime;
}

vector<mint> factorial_inv(int n){
    vector<mint> inv_fac(n + 1, 1);
    mint n_fac_inv = 1;
    for (int i = 2; i <= n; ++i){
        n_fac_inv *= mint(i);
    }
    n_fac_inv = n_fac_inv.inv();
    for (int i = n; i >= 1; --i){
        inv_fac[i] = n_fac_inv;
        n_fac_inv *= mint(i);
    }
    return inv_fac;
}

int main(){
    cin.tie(nullptr);
    ios::sync_with_stdio(false);

    int N;
    if (!(cin >> N)) return 0;
    
    vector<mint> f(N + 1, 0);
    vector<mint> g(N + 1, 0);
    vector<int> primes = sieve_of_eratosthenes(N);
    vector<mint> fac_inv = factorial_inv(N);
    for (int p : primes){
        f[p] = fac_inv[p - 1];
    }
    g[0] = 1;
    for (int p : primes){
        g[p] = fac_inv[p];
    }
    vector<mint> g_pow = pow_fps(g, N - 1, N + 1);

    vector<mint> a = convolution(f, g_pow);
    
    mint ans = a[N - 1];
    for (int i = 1; i <= N - 2; ++i){
        ans *= mint(i);
    }
    cout << ans.val() << "\n";
    return 0;
}