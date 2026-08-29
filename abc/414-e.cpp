#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
using mint = modint998244353;
typedef long long ll;
int main(){
    ll N;
    cin >> N;
    mint ans = mint(N)*(N+1)/2;
    //これから、aがbで割り切れる場合を引く
    for (ll i = 1; i < 3e6; i++){
        //商が小さいとき
        ans -= mint(ll(N/i) - ll(N/(i+1))) * i;
        //商が大きいとき
        if (N/i >= 3e6){
            ans -= mint(N/i);
        }
    }
    cout << ans.val() << endl;
}
