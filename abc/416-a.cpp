#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
int main(){
    int N,L,R;
    cin >> N >> L >> R;
    string s;
    cin >> s;
    bool ok = true;
    for (int i = L-1; i<R;i++){
        if (s[i] == 'x'){
            ok = false;
            break;
        }
    }
    if (ok){
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}