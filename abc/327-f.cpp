#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using mint = modint998244353;
using ll = long long;
using S  = pair<int,int>;
//RMQandRAQ
int e(){
    return 0;
}
int op(int u,int v){
    return max(u,v);
}
int mapping(int f,int x){
    return f+x;
}
int composition(int f,int g){
    return f+g;
}
int id(){
    return 0;
}
int main(){
    int N,D,W;
    cin >> N >> D >> W;
    vector<S> apples;
    for (int i=0;i<N;i++){
        int T,X;
        cin >> T >> X;
        apples.push_back({T,X});
    }
    sort(apples.begin(),apples.end());
    deque<S> d;
    for (int i=0;i<N;i++){
        d.push_back(apples[i]);
    }
    lazy_segtree<int, op, e, int, mapping, composition, id> seg(4*(100000)+2);
    int ans = 0;
    for (int i=0;i<N;i++){
        int T,X;
        T = apples[i].first;
        X = apples[i].second;
        seg.apply(X,X+W,1);
        while (true){
            int s,k;
            s = d.front().first;
            k = d.front().second;
            if (s<=T-D){
                seg.apply(k,k+W,-1);
                d.pop_front();
            }else{
                break;
            }
        }
        int temp = seg.all_prod();
        if (temp>ans){
            ans = temp;
        }
    }
    cout << ans << endl;
}
