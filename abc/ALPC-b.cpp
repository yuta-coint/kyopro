#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using ll = long long;
int main(){
    int N,Q;
    cin >> N >> Q;
    fenwick_tree<ll> fw(N);
    for (int i=0;i<N;i++){
        int a;
        cin >> a;
        fw.add(i,a);
    }
    for (int i=0;i<Q;i++){
        int query;
        cin >> query;
        if (query==0){
            int p,x;
            cin >> p >> x;
            fw.add(p,x);
        }else{
            int l,r;
            cin >> l >> r;
            cout << fw.sum(l,r) << endl;
        }
    }
}