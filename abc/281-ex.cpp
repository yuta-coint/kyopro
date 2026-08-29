#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <atcoder/convolution>
#include <atcoder/modint>

using namespace std;
using namespace atcoder;

using mint = modint998244353;
vector<int> generate_dfs_order(int n) {
    vector<int> res;
    // dfs(現在のノード, 深さ)
    auto dfs = [&](auto self, int k, int depth) -> void {
        if (depth > n) return;

        // 行きがけ (Pre-order)
        res.push_back(k);

        // 深さ n に達するまで子を探索
        if (depth < n) {
            self(self, 2 * k, depth + 1);     // 左の子
            self(self, 2 * k + 1, depth + 1); // 右の子
        }

        // 帰りがけ (Post-order) は負の数で表現
        res.push_back(-k);
    };

    dfs(dfs, 1, 1);
    return res;
}

int main() {
    // 高速I/O
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int N;
    int POW = 0;
    long long A;
    cin >> N >> A;
    int two_power_POW = 1;
    while (N >= two_power_POW){
        two_power_POW *= 2;
        POW++;
    }
    //fを構築する
    vector<mint> f(two_power_POW, 1);
    mint fracn = 1;
    f[0] = 1;
    for (int i = 1; i < two_power_POW; i++){
        f[i] = f[i - 1] * (A - i + 1); 
        fracn *= i; 
    }
    fracn = fracn.inv();
    for (int i = two_power_POW - 1 ; i >= 0; i--){
        f[i] *= fracn;
        fracn *= i;
    }

    vector<mint> ans(two_power_POW, 0);
    //[l,r)の積を求める。
    vector<vector<mint>> dp(two_power_POW * 2, {1});
    //fと[0,l)の積の次数が[l,r)の部分を求める。
    vector<vector<mint>> g(two_power_POW * 2, {1});
    vector<int> dfs_order = generate_dfs_order(POW + 1);
    vector<int> l(two_power_POW * 2, 0);
    vector<int> r(two_power_POW * 2, 0);
    for (int i = 0; i < dfs_order.size(); i++){
        int k = dfs_order[i];
        if (k == 1){
            g[1] = f;
            r[1] = two_power_POW;
        }else if (k > 0){
            //gの更新を行う
            if (k%2 == 0){
                l[k] = l[k/2];
                r[k] = (l[k] + r[k/2]) / 2;
                //g(k) = g(k/2)前半部分
                g[k] = vector<mint>(g[k/2].begin(), g[k/2].begin() + (r[k] - l[k]));
            }else{
                l[k] = (l[k/2] + r[k/2]) / 2;
                r[k] = r[k/2];
                g[k] = convolution(g[k/2], dp[k - 1]);
                //g(k) = g(k/2)のr[k]-l[k]から、2(r[k]-l[k])までの部分
                g[k] = vector<mint>(g[k].begin() + r[k] - l[k], g[k].begin() + 2 * (r[k] - l[k]));
            }
        }else{
            k = -k;
            //dpの更新を行う。
            if (k < two_power_POW){
                dp[k] = convolution(dp[2 * k], dp[2 * k + 1]);
            }else if(k < two_power_POW + 2){
                dp[k] = {1,0};
            }else{
                dp[k] = {1,g[k][0]};
            }
        }
    }
    cout << g[two_power_POW + N][0].val() << "\n";
    return 0;
}