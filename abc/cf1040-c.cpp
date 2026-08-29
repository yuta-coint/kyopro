#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int solve(){
    int N;
    cin >> N;
    vector<tuple<int,int,int>> AB(N);
    for (int i = 0; i < N; i++){
        int a,b;
        cin >> a >> b;
        AB[i] = make_tuple(a,-b,i+1);
    }
    sort(AB.begin(), AB.end());
    int k = 0;
    vector<int> ans;
    int ma = 0;
    int last = -1;
    for (int i = 0; i < N; i++){
        int a,b,c;
        tie(a,b,c) = AB[i];
        b = -b;
        if (b < ma){
            continue;
        }else{
            ma = b;
            k++;
            ans.push_back(c);
        }
    }
    sort(ans.begin(), ans.end());
    cout << k << endl;
    if (k == 0){
        cout << endl;
        return 0;
    }else{
        for (int i = 0; i < k-1; i++){
            cout << ans[i] << " ";
        }
        cout << ans[k-1] << endl;
    }
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