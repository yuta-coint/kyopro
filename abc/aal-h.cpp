#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using mint = modint998244353;
# define ll long long
//足す、割るかどうか、足す。
vector<ll> e(){
    return {0,0,0};
}

vector<ll> op(vector<ll> u,vector<ll> v){
    vector<ll> r(3);
    if (u[1]== 0 && v[1] == 0){
        return {0,0,u[0] + u[2] + v[0] + v[2]};
    }else if (u[1]== 1 && v[1] == 0){
        return {u[0],1,u[2] + v[0] + v[2]};
    }else{
        return {u[0] + u[2] + v[0],1,v[2]};
    }
    return r;
}


int main(){
    int N,Q;
    cin >> N >> Q;
    vector<vector<ll>> start(N);
    vector<ll> A(N);
    for (int i=0;i<N;i++){
        cin >> A[i];
        if (A[i] == 0){
            start[i] = {0,1,0};
        }else{
            start[i] = {0,0,A[i]};
        }
    }
    
    segtree<vector<ll>,op,e> seg(start);
    
    vector<ll> ans(3);
    for (int q=0;q<Q;q++){
        ll T;
        cin >> T;
        if (T==1){
            ll i,x;
            cin >> i >> x;
            if (x == 0){
                seg.set(i - 1,{0,1,0});
            }else{
                seg.set(i - 1,{0,0,x});
            }
        }else{
            int l,r;
            cin >> l >> r;
            ll x;
            cin >> x;
            ans = seg.prod(l-1,r);
            //cout << ans[0] << " " << ans[1] << " " << ans[2] << endl;
            if (ans[1] == 0){
                cout << x + ans[0] + ans[2] << endl;
            }else{
                cout << (x + ans[0]) % 998244353 + ans[2] << endl;
            }
        }
    }
}