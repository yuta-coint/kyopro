#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int solve(){
    string s;
    cin >> s;
    int n = s.size();
    ll ans = pow(2,63);
    int seq_zero = 0;
    int remaining_zeros = 0;
    int cnt_one = -1;
    for (int i = 0; i < n; ++i){ 
        if (s[i] == '0'){
            remaining_zeros++;
        }
    }
    ll tmp;
    for (int i = 0; i < n; ++i){
        if (s[i] == '0'){
            seq_zero++;
            remaining_zeros--;
        } else {
            tmp = (ll(seq_zero) + ll(remaining_zeros) + ll(cnt_one))*pow(10,12)+ll(remaining_zeros) + ll(cnt_one);
            //cout << seq_zero << " " << remaining_zeros << " " << cnt_one << " " << tmp << endl;
            if (tmp< ans && cnt_one >= 0){
                ans = tmp;
            }
            cnt_one++;
            seq_zero = 0;
        }
    }
    tmp = (ll(seq_zero) + ll(remaining_zeros) + ll(cnt_one))*pow(10,12)+ll(remaining_zeros) + ll(cnt_one);
    if (tmp < ans && cnt_one >= 0){
        ans = tmp;
    }
    cnt_one += 1;
    tmp = ll(cnt_one) * pow(10,12) + ll(cnt_one);
    if (tmp < ans && cnt_one >= 0){
        ans = tmp;
    }
    cout << ans << endl;
    return 0;
}
int main(){
    int T;
    cin >> T;
    while (T--){
        solve();
    }
}