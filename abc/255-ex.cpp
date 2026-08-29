#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using mint = modint998244353;
using ll = long long;
ll mod = 998244353;
//usingつかって型の名前各階数減らした方が良かったな
pair<mint,mint> e(){
    return {0,0};
}
pair<mint,mint> op(pair<mint,mint> u,pair<mint,mint> v){
    return {u.first+v.first,u.second+v.second};
}
pair<mint,mint> mapping(pair<bool,ll> f,pair<mint,mint> x){
    if (f.first == true){
        return x;
    }else{
        return {x.second*f.second,x.second};
    }
}
pair<bool,ll> composition(pair<bool,ll> f,pair<bool,ll> g){
    if (f.first == true){
        return f;
    }else{
        return g;
    }
}
pair<bool,ll>id(){
    return {true,0};
}
int main(){
    ll N,Q;
    cin >> N >> Q;
    vector<ll> D;
    vector<ll> sect;
    for (int i=0;i<Q;i++){
        //全て半開区間にする。
        ll Di,Li,Ri;
        cin >> Di >> Li >> Ri;
        Ri +=1;
        D.push_back(Di);
        sect.push_back(Li);
        sect.push_back(Ri);
    }
    //座標圧縮をしたい
    vector<ll> sectB = sect;
    sort(sectB.begin(),sectB.end());
    sectB.erase(unique(sectB.begin(), sectB.end()), sectB.end());
    //圧縮した後の各パーツについて
    vector<mint> Productivity;
    int Bs = sectB.size();
    for (int i=0;i<Bs-1;i++){
        mint L,R;
        L = mint(sectB[i]);
        R = mint(sectB[i+1]);
        Productivity.push_back((L+R-1)*(R-L)*499122177);
    }
    lazy_segtree<pair<mint,mint>, op, e, pair<bool,ll>, mapping, composition, id> seg(2*Q+1);
    //既に収穫されている分量を記録したい
    //じゃあ作用はアップデート？
    //とりあえず最初の状態を記録しておこう。
    for (int i=0;i<Bs-1;i++){
        seg.set(i,{0,Productivity[i]});
    }
    for (int i=0;i<Q;i++){
        //cout << sect[2*i] << sect[2*i+1] << endl;
        ll l,r;
        //下のコードでなぞにバグる
        //ll p,q = sect[2*i],sect[2*i+1];
        l = lower_bound(sectB.begin(), sectB.end(), sect[2*i]) - sectB.begin();
        r = lower_bound(sectB.begin(), sectB.end(), sect[2*i+1]) - sectB.begin();
        //cout << l << r << endl;
        mint stock,worth;
        tie(stock,worth) = seg.prod(l,r);
        //cout << stock << worth << D[i] << endl;
        mint ans;
        ans = worth*mint(D[i])-stock;
        cout << ans.val() << endl;
        seg.apply(l,r,{false,D[i]});
    }
}