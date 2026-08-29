#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
    int H, W;
    cin >> H >> W;
    vector<vector<ll>> grid(H, vector<ll>(W));
    for (int i = 0; i < H; i++){
        for (int j = 0; j < W; j++){
            cin >> grid[i][j];
        }
    }
    ll ok = pow(10, 18);
    ll ng  = -1;
    vector<ll> P(H + W -1);
    for (int i = 0; i < H + W - 1; i++){
        cin >> P[i];
    }
    while (ok - ng > 1){
        ll mid = (ok + ng) / 2;
        vector<vector<ll>> dp(H, vector<ll>(W, -1));
        //持ち込めるコインの枚数
        dp[0][0] = mid;
        for (int i = 0; i < H; i++){
            for (int j = 0; j < W; j++){
                if (dp[i][j] < 0){
                    continue;
                }
                dp[i][j] += grid[i][j]-P[i + j];
                //if (mid < 20){
                //    cout << dp[i][j] << " "<< i << " " << j << endl;
                //}
                if (dp[i][j] < 0){
                    continue;
                }
                if (i + 1 < H){
                    dp[i + 1][j] = max(dp[i + 1][j], dp[i][j]);
                }
                if (j + 1 < W){
                    dp[i][j + 1] = max(dp[i][j + 1], dp[i][j]);
                }
            }
        }
        if (dp[H - 1][W - 1] >= 0){
            ok = mid;
        } else {
            ng = mid;
        }
    }
    cout << ok << endl;
    return 0;
}