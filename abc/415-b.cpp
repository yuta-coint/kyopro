#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
    string s;
    cin >> s;
    int n = s.size();
    vector<int> ans;
    for (int i = 0; i < n; ++i){
        if (s[i] == '#'){
            ans.push_back(i + 1);
        }
    }
    int m = ans.size()/2;
    for (int i = 0; i < m; ++i){
        cout << ans[2*i] << "," << ans[2*i+1] << endl;
    }
}