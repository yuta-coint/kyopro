//https://drken1215.hatenablog.com/entry/2021/08/09/235400
#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using mint = modint998244353;
# define ll long long
vector<ll> e(){
    return {0,0};
}

vector<ll> op(vector<ll> u,vector<ll> v){
    vector<ll> r(2);
    r[0] = u[0]+v[0];
    r[1] = u[1]+v[1];
    return r;
}

vector<ll> mapping(int f,vector<ll> x){
    if (f==0){
        return x;
    }else{
        return {x[1] - x[0],x[1]};
    }
}

int composition(int f,int g){
    return f^g;
}

int id(){
    return 0;
}
int main() {

    int Q;
    cin >> Q;
    vector<int> Ts(Q);
    vector<ll> A(2*Q);

    // 座標圧縮したい数列
    for (int q = 0; q < Q;q++){
        int T;
        ll l,r;
        cin >> T >> l >> r;
        Ts[q] = T;
        A[2 * q] = l - 1;
        A[2 * q + 1] = r;
    }

    // コピー
    vector<ll> B = A;
    
    // B を小さい順にソート
    sort(B.begin(), B.end());
    
    // B から重複を除去する (A が相異なるときは省略可)
    B.erase(unique(B.begin(), B.end()), B.end());

    // 座標圧縮した結果を求める
    vector<ll> res(2 * Q);
    for (int i = 0; i < 2 * Q; ++i) {
        res[i] = lower_bound(B.begin(), B.end(), A[i]) - B.begin();
    }

    int N = B.size() - 1;
    vector<vector<ll>> start(N);
    for (int i = 0; i < N; ++i){
        start[i] = {0,B[i + 1] - B[i]};
    }

    lazy_segtree<vector<ll>, op, e, int, mapping, composition, id> seg(start);

    vector <ll> ans(2);
    for (int q=0;q<Q;q++){
        if (Ts[q]==1){
            seg.apply(res[2 * q],res[2 * q + 1],1);
        }else{
            ans = seg.prod(res[2 * q],res[2 * q + 1]);
            cout << ans[0] << endl;
        }
    }
}