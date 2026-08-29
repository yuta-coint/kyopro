#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using ll = long long;
int main(){
    int N,X;
    cin>>N>>X;
    vector<int> a,b,c;
    vector<int> f(X+1);
    a = {};
    int t;
    for (int i=0;i<N;i++){
        cin >> t;
        a.push_back(t);
        f[t]+=1;
    }
    f = {};
    g = convolution<998244353>(f,f);
    g = convolution<998244353>(f,g);
    int cnt;
    cnt = 0
    for (int x=0;x<X;x++){
        if (f[x]>=2){
            if (X==3*x){
                cnt+=f[x]*(f[x]-1)*(f[x]-2)/6
            }else if (0<=X-2*x){
                cnt+=f[x]*(f[x]-1)*f[X-2*x]*3/2
            }
        }
    }
    cout << c[n+m-2] << endl;
}