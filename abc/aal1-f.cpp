#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using mint = modint998244353;
# define ll long long
//長さ、左、右、全体
vector<ll> e(){
    return {0,-1,0,-1,0,-1,0};
}

vector<ll> op(vector<ll> u,vector<ll> v){
    vector<ll> r(7);
    r[0] = u[0]+v[0];

    r[1] = u[1];
    if (u[0] == u[2] && v[1] == u[1]){
        r[2] = u[2] + v[2];
    }else{
        r[2] = u[2];
    }

    r[3] = v[3];
    if (v[4] == v[0] && v[3] == u[3]){
        r[4] = u[4] + v[4];
    }else{
        r[4] = v[4];
    }
    r[5] = -1;
    r[6] = 0;
    if (u[6] > r[6]){
        r[5] = u[5];
        r[6] = u[6];
    }
    if (v[6] > r[6]){
        r[5] = v[5];
        r[6] = v[6];
    }
    if (u[3] == v[1] && u[4] + v[2] > r[6]){
        r[5] = u[3];
        r[6] = u[4] + v[2];
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
    }
    for (int i=0;i<N;i++){
        start[i] = {1,A[i],1,A[i],1,A[i],1};
    }
    
    segtree<vector<ll>,op,e> seg(start);
    
    vector<ll> ans(7);
    for (int q=0;q<Q;q++){
        ll T,L,R;
        cin >> T>> L >> R;
        if (T==1){
            L--;
            seg.set(L,{1,R,1,R,1,R,1});
        }else{
            ans = seg.prod(L-1,R);
            cout << ans[6] << endl;
        }
    }
}