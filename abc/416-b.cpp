#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
int main(){
    string s;
    cin >> s;
    int L;
    L = s.size();
    vector<char> ans;
    bool chk = true;
    for (int i = 0; i < L; i++){
        if (s[i] == '.'){
            if (chk){
                ans.push_back('o');
                chk = false;
            }else{
                ans.push_back('.');
            }
        }else{
            ans.push_back('#');
            chk = true;
        }
    }
    for (char c : ans){
        cout << c;
    }
}