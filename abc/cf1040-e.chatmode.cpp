#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int solve(){
    int N;
    cin >> N;
    ng = 0;
    ok = 1001;
    while (ok - ng > 1){
        int mid = (ok + ng) / 2;
        cout << "?" << " " << mid;
        for (int i = 0; i < mid; i++){
            cout << " " << i+1;
        }
        cout.flush();
        int x;
        cin >> x;
        if (x == 0){
            ng = mid;
        }else{
            ok = mid;
        }
    }
    if (ok == 1001){
        int R = 1;
    }else{
        int R = ok;
    }
    vector<char> ans(N);
    for (int i = 0; i < 125; i++){
        cout << "?" << " " << 510;
        for (int j = 8*i+1; j < 8*(i+1)+1; j++){
            for (int k = 0; k < pow(2,(j-8*i-1)); k++){
                if (j > N){
                    cout << " " << R;
                }else{
                cout << " " << j;
                }
            }
        }
        for (int j = 0; j < 255; j++){
            cout << " " << R;
        }
        cout.flush();
        int x;
        cin >> x;
        for (int j = 8*i+1; j < 8*(i+1)+1; j++){
            if (j > N){
                ans[R-1] = ")";
                continue;
            }
            if ((x >> (j - 8*i - 1)) & 1){
                    ans[j-1] = "(";
                }else{
                    ans[j-1] = ")";
            }
        }
    cout << "!" << " ";
    for (int j = 0; j < N; j++){
        cout << ans[j];
    }
}
int main(){
    int T;
    cin >> T;
    for (int i = 0; i < T; i++){
        solve();
    }
    return 0;
}