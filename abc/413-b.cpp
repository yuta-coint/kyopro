#include <bits/stdc++.h>
#include <unordered_set>
using namespace std;
typedef long long ll;
int main(){
    int N;
    cin >> N;
    vector<string> S;
    string s;
    for (int i = 0; i < N ;++i){
        cin >> s;
        S.push_back(s);
    }
    string s_sum;
    unordered_set<string> ans;
    for (int i = 0; i < N ;++i){
        for (int j = 0; j < N; ++j){
            if (i == j){
              continue;
            }
            s_sum = S[i] + S[j];
            //cout << s_sum << endl;
            ans.insert(s_sum);
        }
    }
    cout << ans.size() << endl;
}