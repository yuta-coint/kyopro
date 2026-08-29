#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
    int n;
    cin >> n;
    vector<int> a;
    bool ans;
    for (int i = 0; i < n; ++i){
        int tmp;
        cin >> tmp;
        a.push_back(tmp);
    }
    int x;
    cin >> x;
    ans = false;
    for (int i = 0; i < n; ++i){
        if (a[i] == x){
            ans = true;
            break;
        }
    }
    if (ans){
        cout << "Yes" << endl;
    } else {
        cout << "No" << endl;
    }
}