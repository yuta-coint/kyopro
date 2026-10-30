#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using mint = modint998244353;
vector<mint> e(){
    return {0,0,0,0,0};
}

vector<mint> op(vector<mint> u,vector<mint> v){
    vector<mint> r(5);
    r[0] = u[0] + v[0];
    r[1] = u[1] + v[1];
    r[2] = u[2] + v[2];
    r[3] = u[3] + v[3];
    r[4] = u[4] + v[4];
    return r;
}

vector<mint> mapping(mint f,vector<mint> x){
    vector<mint> r(5);
    r[4] = f * f * f * f * x[0] + 4 * x[1] * f * f * f + 6 * x[2] * f * f + 4 * x[3] * f + x[4];
    r[3] = f * f * f * x[0] + 3 * x[1] * f * f + 3 * x[2] * f + x[3];
    r[2] = f * f * x[0] + 2 * x[1] * f + x[2];
    r[1] = f * x[0] + x[1];
    r[0] = x[0];
    return r;
}

mint composition(mint f,mint g){
    return f + g;
}

mint id(){
    return 0;
}

int main(){
    int N,Q;
    cin >> N >> Q;
    vector<vector<mint>> start(N);
    for (int i=0;i<N;i++){
        int a;
        cin >> a;
        mint A = mint(a);
        start[i] = {mint(1),A,A*A,A*A*A,A*A*A*A};
    }
    
    lazy_segtree<vector<mint>, op, e, mint, mapping, composition, id> seg(start);
    
    vector<mint> ans(5);
    // ans = seg.prod(1,1);
    // cout << ans[0].val() << endl;

    for (int q=0;q<Q;q++){
        int T,L,R;
        cin >> T>> L >> R;
        if (T==1){
            int x;
            cin >> x;
            seg.apply(L - 1, R, mint(x));
        }else{
            int k;
            cin >> k;
            ans = seg.prod(L-1,R);
            cout << ans[k].val() << endl;
        }
    }
}