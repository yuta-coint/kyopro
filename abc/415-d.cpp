#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
//少ないコーラ瓶の消費量でシールがもらえると嬉しい
int main(){
    ll n, m;
    cin >> n >> m;
    vector<pair<ll,ll>> line_up(m);
    for (int  i = 0; i < m; i++){
        ll a,b;
        cin >> a >> b;
        line_up[i] = {a-b, a};
    }
    sort(line_up.begin(), line_up.end());
    ll ans = 0;
    for (int i = 0; i < m; i++){
        if (n < line_up[i].second){
            continue;
        }
        ll buy = (n - line_up[i].second) / line_up[i].first + 1;
        ans += buy;
        n -= buy * line_up[i].first;
    }
    cout << ans << endl;
    return 0;
}