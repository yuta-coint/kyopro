#include <bits/stdc++.h>
using namespace std;
void solve(){
    int N;
    cin >> N;
    vector<int> P;
    for (int i = 0; i< (1<<N); ++ i){
        int p;
        cin >> p;
        P.push_back(p);
    }
    vector<int> dp(1<<(N+1), 0);
    for (int i = (1<<(N+1))-1; i>=1; -- i){
        if (i >=(1<<N)){
            dp[i] = P[i-(1<<N)];
        }else{
            dp[i] = min(dp[2*i],dp[2*i+1]);
        }
    }
    stack<int> S;
    S = stack<int>();
    S.push(1);
    vector<int> ans;
    while (!S.empty()){
        int i = S.top();
        //cout << i << " ";
        S.pop();
        if (i >= (1<<N)){
            ans.push_back(dp[i]);
            continue;
        }
        if (dp[2*i] == dp[i]){
            S.push(2*i+1);
            S.push(2*i);
        }else{
            S.push(2*i);
            S.push(2*i+1);
        }
    }
    //cout << endl;
    for (int i = 0; i< (1<<N); ++ i){
        cout << ans[i] << " ";
    }
    cout << endl;
}
int main(){
    int T;
    cin >> T;
    while (T--) {
        solve();
    }
}