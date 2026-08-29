#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using ll = long long;
int main(){
    int n,m;
    cin>>n>>m;
    vector<int> a,b,c;
    a = {};
    b = {};
    int t;
    for (int i=0;i<n;i++){
        cin >> t;
        a.push_back(t);
    }
    for (int i=0;i<m;i++){
        cin >> t;
        b.push_back(t);
    }
    c = convolution<998244353>(a,b);
    for (int i=0;i<n+m-2;i++){
        cout << c[i]<<" ";
    }
    cout << c[n+m-2] << endl;
}