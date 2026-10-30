//https://drken1215.hatenablog.com/entry/2021/08/09/235400
#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using mint = modint998244353;
# define ll long long
vector<ll> e(){
    return {0,0,0};
}
//個数と合計とスコア
vector<ll> op(vector<ll> left,vector<ll> right){
    return {left[0] + right[0], left[1] + right[1],(left[2] + right[2] + left[0] * right[1]%998244353)%998244353};
}

int main() {
    int N,Q;
    cin >> N >> Q;
    vector<int> Ts(Q);
    vector<ll> xs(Q);
    vector<ll> zaatu(N + Q);
    vector<ll> A(N);

    // 座標圧縮したい数列
    for (int i = 0; i < N;i++){
        cin >> A[i];
        zaatu[i] = A[i];
    }

    for (int q = 0; q < Q;q++){
        int T;
        cin >> T;
        Ts[q] = T;
        if (T <= 2){
            cin >> xs[q];
        }else{
            xs[q] = 0;
        }
        zaatu[N + q] = xs[q];
    }

    // コピー
    vector<ll> B = zaatu;
    
    // B を小さい順にソート
    sort(B.begin(), B.end());
    
    // B から重複を除去する (A が相異なるときは省略可)
    B.erase(unique(B.begin(), B.end()), B.end());

    // 座標圧縮した結果を求める
    vector<ll> res(N + Q);
    for (int i = 0; i < N + Q; ++i) {
        res[i] = lower_bound(B.begin(), B.end(), zaatu[i]) - B.begin();
    }

    int M = B.size();
    vector<ll> cnt(M,0);
    for (int i = 0; i < N; ++i){
        cnt[res[i]] += 1;
    }
    
    ll half = 499122177;
    ll mod = 998244353;
    vector<vector<ll>> start(M);
    for (int i = 0; i < M; ++i){
        start[i] = {cnt[i], B[i] * cnt[i], B[i] * cnt[i] %mod * (cnt[i] + 1)%mod * half %mod};
    }

    segtree<vector<ll>, op, e> seg(start);
    vector<ll> ans(3);
    for (int q=0;q<Q;q++){
        if (Ts[q]==1){
            vector<ll> now = seg.get(res[q + N]);
            ll t = now[0] + 1;
            seg.set(res[q + N],{t, B[res[q + N]] * t, B[res[q + N]] * t %mod * (t + 1)%mod * half %mod});
        }else if(Ts[q] == 2){
            vector<ll> now = seg.get(res[q + N]);
            ll t = now[0] - 1;
            seg.set(res[q + N],{t, B[res[q + N]] * t, B[res[q + N]] * t %mod * (t + 1)%mod * half %mod});
        }else{
            ans = seg.all_prod();
            cout << ans[2]%mod << endl;
        }
    }
}