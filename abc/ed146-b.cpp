#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int calc(ll a,ll b,long x){
    return x+1+(a-1)/x + (b-1)/x;
}
int main(){
    int t;cin>>t;
    for (int ca=0;ca<t;ca++){
        ll a;ll b;
        cin >> a >> b;
        ll ans;
        ans = pow(10,16);
        for (long x=1;x<pow(10,5);x++){
            if (calc(a,b,x)<ans){
                ans = calc(a,b,x);
            }
        }
        cout << ans <<endl;
    }
}