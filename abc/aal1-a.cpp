//https://atcoder.jp/contests/practice2/submissions/42057728
#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
long e(){
    return(1000000000);
}
long op(long a,long b){
    return min(a,b);
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
            //LR間の最小値
            cin >> L >> R;
            long ans;
            ans = seg.prod(L-1,R);
            cout << ans << endl;
        }
    }
}