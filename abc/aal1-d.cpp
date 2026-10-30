#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using mint = modint998244353;
# define ll long long
vector<ll> e(){
    return {0,0,0,0};
}
//個数と合計とスコア
vector<ll> op(vector<ll> left,vector<ll> right){
    return {left[0] + right[0], left[1] + right[1],left[2] + right[2],left[3] + right[3] + left[2] * (right[0] + right[1]) + left[1] * (right[0])};
}


int main(){
    int N,Q;
    cin >> N >> Q;
    vector<vector<ll>> start(N);
    for (int i=0;i<N;i++){
        int Ai;
        cin >> Ai;
        if (Ai == 0){
            start[i] = {1,0,0,0};
        }else if(Ai == 1){
            start[i] = {0,1,0,0};
        }else{
            start[i] = {0,0,1,0};
        }
    }
    segtree<vector<ll>, op, e> seg(start);
    vector <ll> ans(4);
    for (int q=0;q<Q;q++){
        int T,L,R;
        cin >> T>> L >> R;
        if (T==1){
            if (R == 0){
                seg.set(L - 1,{1,0,0,0});
            }else if(R == 1){
                seg.set(L - 1,{0,1,0,0});
            }else{
                seg.set(L - 1,{0,0,1,0});
            }
        }else{
            ans = seg.prod(L-1,R);
            cout << ans[3] << endl;
        }
    }
}