//https://atcoder.jp/contests/practice2/submissions/42057728
#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
# define ll long long
ll e(){
    return 0;
}
ll op(ll a,ll b){
    return a + b;
}
ll target;
bool f(ll v) { return v < target; }

int main(){
    int N,Q;
    cin >> N >> Q;
    vector<ll> A = {};
    segtree<ll,op,e> seg(N);
    for (int i=0;i<N;i++){
        ll a;
        cin >>a;
        seg.set(i,a);
    }
    for (int q=0;q<Q;q++){
        int T;
        cin >> T;
        if (T==1){
            ll X,V;
            //X項目をVに更新
            cin >> X >> V;
            seg.set(X-1,V);
        }else if(T==2){
            int L;
            cin >> L >> target;
            int ans;
            ans = seg.max_right<f>(L - 1) + 1;
            cout << ans << endl;
        }else{
            int R;
            cin >> R >> target;
            int ans;
            ans = seg.min_left<f>(R);
            cout << ans << endl;
        }
    }
}