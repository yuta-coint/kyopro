#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <atcoder/convolution>
#include <atcoder/modint>

using namespace std;
using namespace atcoder;

using mint = modint998244353;
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



pair<vector<mint>,vector<mint>> rational_sum(const vector<vector<mint>>& P, const vector<vector<mint>>& Q, long long N) {
    if (N == 1){
        return {P[0], Q[0]};
    }
    vector<mint> P1,Q1, P2,Q2;
    //前半と後半についての総和を考える。短く切って渡す
    vector<vector<mint>> P_half, Q_half;
    int half = (int)P.size() / 2;
    for (int i = 0; i < half; i++){
        P_half.push_back(P[i]);
        Q_half.push_back(Q[i]);
    }
    pair<vector<mint>,vector<mint>> half_sum = rational_sum(P_half, Q_half, half);
    P1 = half_sum.first;
    Q1 = half_sum.second;
    P_half.clear();
    Q_half.clear();
    for (int i = half; i < (int)P.size(); i++){
        P_half.push_back(P[i]);
        Q_half.push_back(Q[i]);
    }
    half_sum = rational_sum(P_half, Q_half, N - half);
    P2 = half_sum.first;
    Q2 = half_sum.second;
    P_half.clear();
    Q_half.clear();
    vector<mint> resQ = convolution(Q1, Q2);
    vector<mint> resP = convolution(P1, Q2);
    vector<mint> P_add = convolution(Q1, P2);
    if (resP.size() < P_add.size()) resP.resize(P_add.size(), 0);
    for (int i = 0; i < (int)P_add.size(); i++){
        resP[i] += P_add[i];
    }
    return {resP, resQ};
}
int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N, M, K;
    cin >> N >> M >> K;
    vector<mint> A(N), B(M);
    for (int i = 0; i < N; i++){
        int a;
        cin >> a;
        A[i] = mint(a);
    }
    for (int i = 0; i < M; i++){
        int b;
        cin >> b;
        B[i] = mint(b);
    }
    vector<vector<mint>> F_C;
    vector<vector<mint>> G_C;
    for (int i = 0; i < N; i++){
        F_C.push_back({1});
        G_C.push_back({1,-A[i]});
    }
    pair<vector<mint>,vector<mint>> C_frac = rational_sum(F_C, G_C, N);
    vector<mint> C = convolution(C_frac.first, inv_fps(C_frac.second, K + 1));
    C.resize(K + 1);
    vector<vector<mint>> F_D;
    vector<vector<mint>> G_D;
    for (int i = 0; i < M; i++){
        F_D.push_back({1});
        G_D.push_back({1,-B[i]});
    }
    pair<vector<mint>,vector<mint>> D_frac = rational_sum(F_D, G_D, M);
    vector<mint> D = convolution(D_frac.first, inv_fps(D_frac.second, K + 1));
    D.resize(K + 1);
    mint fac = 1;
    for (int i = 1; i < K + 1; i++){
        fac *= i;
    }
    fac = fac.inv();
    for (int i = K; i >= 0; i--){
        C[i] *= fac;
        D[i] *= fac;
        fac *= i;
    }
    vector<mint> ans = convolution(C, D);
    ans.resize(K + 1);
    fac = 1;
    mint mother = mint(M) * mint(N);
    mother = mother.inv();
    for (int i = 1; i < K + 1; i++){
        ans[i] *= fac;
        ans[i] *= mother;
        fac *= i + 1;
        cout << ans[i].val() << "\n";
    }
    return 0;
}
