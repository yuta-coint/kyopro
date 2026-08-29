#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
long e(){
    return(-1);
}
long op(long a,long b){
    return max(a,b);
}
long V;
bool check(long x){
    if (x<V){
        return(true);
    }else{
        return(false);
    }
}
int main(){
    int N,Q;
    cin >> N >> Q;
    vector<long> A = {};
    segtree<long,op,e> seg(N);
    for (int i=0;i<N;i++){
        long a;
        cin >>a;
        seg.set(i,a);
    }
    for (int q=0;q<Q;q++){
        int T;
        cin >> T;
        if (T==1){
            long X,V;
            //X項目をVに更新
            cin >> X >> V;
            seg.set(X-1,V);
        }else if(T==2){
            int L,R;
            //LR間の最大値
            cin >> L >> R;
            long ans;
            ans = seg.prod(L-1,R);
            cout << ans << endl;
        }else{
            long X;
            cin >> X >> V;
            long ans;
            ans = seg.max_right<check>(X-1)+1;
            cout << ans << endl;
        }
    }
}