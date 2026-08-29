#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int solve(){
    int n;
    cin >> n;
    string s;
    cin >> s;
    vector<bool> realize(1<<n, false);
    realize[0] = true;
    for (int i = 1; i < 1<<n; ++i){
        if (s[i-1] == '0'){
            if (i == 0){
                realize[i] = true;
            } else {
                for (int j = 0; j < n; ++j){
                    if (i & (1<<j)){
                        int prev = i ^ (1<<j);
                        if (realize[prev]){
                            realize[i] = true;
                            break;
                        }
                    }
                }
            }
        }
    }
    if (realize[(1<<n)-1]){
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
    return 0;
}

int main(){
    int T;
    cin >> T;
    while (T--){
        solve();
    }
}