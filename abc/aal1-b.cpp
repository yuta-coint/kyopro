//https://atcoder.jp/contests/practice2/submissions/46238432
#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using namespace std;
# define int long long

int e(){
    return pow(10,16);
}

int op(int u,int v){
    return min(u, v);
}

int mapping(int f,int x){
    return f + x;
}

int composition(int f,int g){
    return f + g;
}

int id(){
    return 0;
}

signed main(){
    int N,Q;
    cin >> N >> Q;
    vector<int> start(N);
    for (int i=0;i<N;i++){
        int Ai;
        cin >> Ai;
        start[i] = Ai;
    }
    lazy_segtree<int, op, e, int, mapping, composition, id> seg(start);
    for (int q=0;q<Q;q++){
        int T,L,R;
        cin >> T>> L >> R;
        if (T==1){
            int x;
            cin >> x;
            seg.apply(L-1,R,x);
        }else{
            int ans;
            ans = seg.prod(L-1,R);
            cout << ans << endl;
        }
    }
    return 0;
}