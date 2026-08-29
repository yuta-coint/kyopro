#include <bits/stdc++.h>
#include <unordered_set>
using namespace std;
typedef long long ll;
int main(){
    int Q;
    cin >> Q;
    int t;
    ll x,k,c;
    deque<pair<ll,ll>> waiting;
    ll ans;
    for (int q = 0; q<Q;++q){
        cin >> t;
        if (t == 1){
            cin >> c >> x;
            waiting.push_back({x,c});
        }else{
            cin >> k;
            while (k > 0){
                vector<ll,ll> xc = waiting.pop_front();
                x,c = xc.first, xc.second;
                if (k > c){
                    k -= c;
                    ans += c*x;
                }else{
                    ans += k*x;
                    waiting.push_front({x , c - k});
                    k = 0;
                }
            }
            cout << ans << endl;   
        }
    }
}
