#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
    int N;
    int M;
    cin >> N >> M;
    vector<ll> X;
    for (int i = 0; i < N; i++) {
        ll x;
        cin >> x;
        X.push_back(x);
    }

    sort(X.begin(), X.end());

    vector<ll> X_diff;
    for (int i = 0; i < N-1; i++) {
        X_diff.push_back(X[i+1] - X[i]);
    }

    sort(X_diff.begin(), X_diff.end());
    ll ans = 0;
    
    for (int i = 0; i < N - M; i++) {
        //cout <<X_diff[i] <<endl;
        ans += X_diff[i];
    }

    cout << ans << endl;
}