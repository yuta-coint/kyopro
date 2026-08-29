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
vector<vector<mint>> multiply2d(const vector<vector<mint>>& A, const vector<vector<mint>>& B) {
    if (A.empty() || A[0].empty() || B.empty() || B[0].empty()) return {};

    int nA = A.size(), mA = A[0].size();
    int nB = B.size(), mB = B[0].size();
    int nRes = nA + nB - 1;
    int mRes = mA + mB - 1;

    // 次の x の次数（次の行）への繰り上がりを防ぐため、ブロック幅を mRes に設定して平坦化
    vector<mint> flatA(nA * mRes, 0);
    for (int i = 0; i < nA; ++i) {
        for (int j = 0; j < mA; ++j) {
            flatA[i * mRes + j] = A[i][j];
        }
    }

    vector<mint> flatB(nB * mRes, 0);
    for (int i = 0; i < nB; ++i) {
        for (int j = 0; j < mB; ++j) {
            flatB[i * mRes + j] = B[i][j];
        }
    }

    // 1次元多項式として畳み込み計算
    // 全要素数を N とすると計算量は O(N log N)
    vector<mint> flatRes = convolution(flatA, flatB);

    // 2次元配列に復元
    vector<vector<mint>> res(nRes, vector<mint>(mRes, 0));
    for (int i = 0; i < nRes; ++i) {
        for (int j = 0; j < mRes; ++j) {
            int idx = i * mRes + j;
            if (idx < (int)flatRes.size()) {
                res[i][j] = flatRes[idx];
            }
        }
    }

    return res;
}
mint Bostan_Mori(const vector<mint>& P, const vector<mint>& Q, long long N) {
    if (N == 0){
        return P[0] / Q[0];
    }
    vector<mint> Q_minus = Q;
    for (int i = 1; i < (int)Q_minus.size(); i += 2){
        Q_minus[i] = -Q_minus[i];
    }
    vector<mint> P_new, Q_new;
    P_new = convolution(P, Q_minus);
    Q_new = convolution(Q, Q_minus);
    vector<mint> P_next, Q_next;
    if (N % 2 == 0){
        for (int i = 0; i < (int)P_new.size(); i += 2){
            P_next.push_back(P_new[i]);
        }
    }else{
        for (int i = 1; i < (int)P_new.size(); i += 2){
            P_next.push_back(P_new[i]);
        }
    }
    for (int i = 0; i < (int)Q_new.size(); i += 2){
        Q_next.push_back(Q_new[i]);
    }
    return Bostan_Mori(P_next, Q_next, N / 2);
}

vector<mint> Bostan_Mori_2d(const vector<vector<mint>>& P, const vector<vector<mint>>& Q, long long N, int target_deg) {
    if (N == 0){
        vector<mint> res = P[0];
        vector<mint> Q_inv = inv_fps(Q[0], target_deg);
        res = convolution(res, Q_inv);
        res.resize(target_deg);
        return res;
    }
    vector<vector<mint>> Q_minus = Q;
    for (int i = 0; i < (int)Q_minus.size(); i++){
        for (int j = 0; j < (int)Q_minus[i].size(); j++){
            if (i % 2 == 1){
                Q_minus[i][j] = -Q_minus[i][j];
            }
        }
    }
    vector<vector<mint>> P_new, Q_new;
    P_new = multiply2d(P, Q_minus);
    Q_new = multiply2d(Q, Q_minus);
    
    long long next_N = N / 2;
    vector<vector<mint>> P_next, Q_next;
    
    for (int i = 0; i <= next_N; i++) {
        int p_idx = i * 2 + (N % 2);
        if (p_idx < (int)P_new.size()) {
            P_next.push_back(P_new[p_idx]);
        } else {
            P_next.push_back(vector<mint>(P_new.empty() ? 1 : P_new[0].size(), 0));
        }
        
        int q_idx = i * 2;
        if (q_idx < (int)Q_new.size()) {
            Q_next.push_back(Q_new[q_idx]);
        } else {
            Q_next.push_back(vector<mint>(Q_new.empty() ? 1 : Q_new[0].size(), 0));
        }
    }
    
    return Bostan_Mori_2d(P_next, Q_next, next_N, target_deg);
}

vector<mint> power_projection(const vector<mint>& F, const vector<mint>& G, int N) {
    vector<vector<mint>> P,Q;
    mint c = F[0];
    for (int i = 0; i < N + 1; i++){
        P.push_back({G[i]});
        if (i == 0){
            Q.push_back({1, 0});
        }else{
            Q.push_back({0, -F[i]});
        }
    }
    vector<mint> h_next = Bostan_Mori_2d(P, Q, N, N + 1);
    //c^{i}/i!を係数に持つ
    vector<mint> h_const;
    mint c_pow = 1;
    for (int i = 0; i < (int)h_next.size(); i++){
        h_const.push_back(c_pow);
        c_pow *= c;
    }
    mint fac = 1;
    for (int i = 1; i < (int)h_next.size(); i++){
        fac *= i;
    }
    fac = fac.inv();
    for (int i = h_next.size() - 1; i >= 0; i--){
        h_next[i] *= fac;
        h_const[i] *= fac;
        fac *= i;
    }
    vector<mint> h = convolution(h_next, h_const);
    h.resize(N + 1);
    fac = 1;
    for (int i = 1; i < (int)h.size(); i++){
        fac *= i;
        h[i] *= fac;
    }
    return h;
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
    int N, M ,L;
    cin >> N >> M >> L;
    vector<int> A(N);
    vector<mint> P(N + 1), Q(N + 1,1);
    mint rev_M = mint(M).inv();
    for (int i = 0; i < M; i++){
        cin >> A[i];
        P[A[i]] = rev_M;
    }
    vector<mint> f = power_projection(P, Q, N - 1);
    f.resize(N + 1, 0);
    vector<vector<mint>> son;
    vector<vector<mint>> mother;
    for (int k = 1; k <= N; k++){
        vector<mint> son_k(1), mother_k(2);
         son_k[0] = (f[k - 1] - f[k]) * f[k - 1].pow(L - 1);
        mother_k[0] = 1;
        if (f[k - 1].val() == 0) {
            // f[k-1] が0のときは分母が定数になるので特例で対応
            mother_k[1] = 0;
        } else {
            mother_k[1] = -f[k] / f[k - 1];
        }
        son.push_back(son_k);
        mother.push_back(mother_k);
    }
    pair<vector<mint>,vector<mint>> res = rational_sum(son, mother, N);
    vector<mint> ans = res.first;
    vector<mint> ans_mother_inv = inv_fps(res.second, L);
    ans = convolution(ans, ans_mother_inv);
    ans.resize(L);
    for (int i = 0; i < L; i++){
        cout << ans[i].val() << endl;
    }
    return 0;
}
