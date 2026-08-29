#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
long e(){
    return(0);
}
long op(long a,long b){
    return a+b;
}
long V;
bool check(long x){
    if (x<V){
        return(true);
    }else{
        return(false);
    }
}
//k種類目の使用枚数をt枚増やす
int main(){
    set<long> alr;
    int N,Q;
    cin >> N;
    vector<long> unit = {};
    vector<long> aveil = {};
    vector<long> key = {};
    for (int i=0;i<N;i++){
        long a,b;
        cin >> a >> b;
        unit.push_back(a);
        aveil.push_back(b);
        key.push_back(a);
    }
    cin >>Q;
    vector<long> queries = {};
    for (int i=0;i<Q;i++){
        long T;
        cin >>T;
        queries.push_back(T);
        if (T==1){
            long x,y;
            cin >> x >> y;
            key.push_back(y);
            queries.push_back(x);
            queries.push_back(y);
        }else if(T==2){
            long x,y;
            cin >> x >> y;
            queries.push_back(x);
            queries.push_back(y);
        }else{
            long x;
            cin >> x;
            queries.push_back(x);
            queries.push_back(-1);
        }
    }
    vector<long> B = key;
    sort(B.begin(), B.end());
    B.erase(unique(B.begin(), B.end()), B.end());
    //どこまで切り取れるか確認してから、seg_pointで切り取って点数計算を行う。
    long L = B.size();
    segtree<long,op,e> seg(L);
    segtree<long,op,e> seg_point(L);
    long s,before;
    for (int i=0;i<N;i++){
        long k = lower_bound(B.begin(), B.end(), unit[i])- B.begin();
        s = aveil[i];
        before = seg.get(k);
        seg.set(k,before+s);
        seg_point.set(k,B[k]*(before+s));
    }
    for (int i=0;i<Q;i++){
        long t,x,y,k;
        t = queries[3*i];
        x = queries[3*i+1];
        y = queries[3*i+2];
        if (t==1){
            x-=1;
            k = lower_bound(B.begin(), B.end(), unit[x]) - B.begin();
            s = -aveil[x];
            before = seg.get(k);
            seg.set(k,before+s);
            seg_point.set(k,B[k]*(before+s));
            //x種類目のカードを0にしたうえでy点のカードを同じ枚数だけ作る
            unit[x] = y;
            k = lower_bound(B.begin(), B.end(), unit[x]) - B.begin();
            s = aveil[x];
            before = seg.get(k);
            seg.set(k,before+s);
            seg_point.set(k,B[k]*(before+s));
        }else if (t==2){
            x-=1;
            k = lower_bound(B.begin(), B.end(), unit[x]) - B.begin();
            s = -aveil[x];
            before = seg.get(k);
            seg.set(k,before+s);
            seg_point.set(k,B[k]*(before+s));
            //x種類目のカードを0にしたうえで
            aveil[x] = y;
            s = aveil[x];
            before = seg.get(k);
            seg.set(k,before+s);
            seg_point.set(k,B[k]*(before+s));
        }else{
            if (seg.all_prod()<x){
                cout << -1 << endl;
            }else{
                V = x;
                long q = seg.min_left<check>(L);
                long amari = x-seg.prod(q,L);
                long ans = seg_point.prod(q,L)+amari*B[q-1];
                cout << ans <<endl;
            }
        }
        
    }
}