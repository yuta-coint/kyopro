#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using ll = long long;
int main(){
    int N,Q;
    cin >> N>>Q;
    dsu d(N);
    for (int i=0;i<Q;i++){
        int t,u,v;
        cin >> t >> u >> v;
        if (t==0){
            d.merge(u,v);
        }else{
            if (d.same(u,v)){
                cout << 1 << endl;
            }else{
                cout << 0 << endl;
            }
        }
    }
}