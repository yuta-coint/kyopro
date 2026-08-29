#include <bits/stdc++.h>
using namespace std;
#define rep(i, n) for (int i = 0; i < (int)(n); i++)
#define rep2(i,k,n) for (int i = k; i < (n); ++i)
int main(){
    int t;cin>>t;
    for(int ca;ca<t;ca++){
        long n;cin >> n;
        vector<int> a(n);
        rep(i,n) {cin >> a[i];}
        sort(a.begin(), a.end());
        long ans = 1;
        rep(i,n-1) {
            if (a[i]<=i && a[i+1]>i+1) {ans++;}
        }
        if (a[0]>0){ans++;}
        cout << ans << endl;
    }
}