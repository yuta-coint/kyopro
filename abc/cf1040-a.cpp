#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int solve(){
    int N;
    cin >> N;
    ll ans = 0;
    for (int i = 0; i < N; i++){
        int x;
        cin >> x;
        if (x == 0){
            ans += 1;
        }else{
            ans += x;
        }
    }
    cout << ans << endl;
    return 0;
}
int main(){
    int T;
    cin >> T;
    for (int i = 0; i < T; i++){
        solve();
    }
    return 0;
}
