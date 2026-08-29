#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main(){
    int t;cin>>t;
    for (int ca=0;ca<t;ca++){
        ll k;ll n;
        cin >> n >> k;
        if (k==1){
            cout << "YES" << endl;
            continue;
        }
        if (n&1){
            if (k&1){
                if (n>=k){
                    cout << "YES" << endl;
                }else{
                    cout << "NO" << endl;
                }
            }else{
                cout << "NO" << endl;
            }
        }else{
            cout << "YES" << endl;
        }
    }
}