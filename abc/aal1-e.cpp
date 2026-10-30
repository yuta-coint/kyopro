#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using mint = modint998244353;
//0の数、1の数、転倒数
vector<mint> e(){
    return {0,0,0,0,0,0};
}

vector<mint> op(vector<mint> u,vector<mint> v){
    vector<mint> r(6);
    r[0] = u[0]+v[0];
    r[1] = u[1]+v[1];
    r[2] = u[2]+v[2];
    r[3] = u[3] + v[3] + u[0] * v[1];
    r[4] = u[4] + v[4] + u[1] * v[2];
    r[5] = u[5] + v[5] + u[0] * v[4] + u[3] * v[2];
    return r;
}


int main(){
    int N,Q;
    cin >> N >> Q;
    vector<mint> temp(6);
    vector<vector<mint>> start(N);
    vector<mint> A(N);
    for (int i=0;i<N;i++){
        int a;
        cin >> a;
        A[i] = mint(a);
    }
    string S;
    cin >> S;
    for (int i=0;i<N;i++){
        char c = S[i];
        if (c == 'R'){
            start[i] = {A[i],0,0,0,0,0};
        }else if (c == 'G'){
            start[i] = {0,A[i],0,0,0,0};
        }else{
            start[i] = {0,0,A[i],0,0,0};
        }
    }
    
    segtree<vector<mint>,op,e> seg(start);
    
    vector<mint> ans(6);
    for (int q=0;q<Q;q++){
        int T,L,R;
        cin >> T>> L >> R;
        if (T==1){
            L--;
            mint x = mint(R);
            if (S[L] == 'R'){
                seg.set(L,{x,0,0,0,0,0});
            }else if (S[L] == 'G'){
                seg.set(L,{0,x,0,0,0,0});
            }else{
                seg.set(L,{0,0,x,0,0,0});
            }
        }else{
            ans = seg.prod(L-1,R);
            cout << ans[5].val() << endl;
        }
    }
}