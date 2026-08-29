#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using mint = modint998244353;
using ll = long long;
using S  = pair<mint,mint>;
//RMQandRAQ
mint e(){
    return 0;
}
mint op(mint u,mint v){
    return u+v;
}
mint mapping(S f,mint x){
    mint a,b;
    a = f.first;b=f.second;
    return a*x+b;
}
S composition(S f,S g){
    mint a,b,c,d;
    a = f.first;b=f.second;c=g.first;d=g.second;
    return {a*c,a*d+b};
}
S id(){
    return {1,0};
}
int main(){
    int N,M;
    cin >> N >> M;
    vector<mint> A(N);
    for (int i=0;i<N;i++){
        int Aj;
        cin >> Aj;
        mint Ai = Aj;
        A[i]=Ai;
    }
    lazy_segtree<mint, op, e, S, mapping, composition, id> seg(A);
    for (int i=0;i<M;i++){
        int L,R,Xi;
        cin >> L >> R >> Xi;
        mint X=Xi;
        S RU;
        mint T = R-L;
        RU = {T/(T+1),X/(T+1)};
        seg.apply(L-1,R,RU);
    }
    mint ans = seg.get(0);
    cout << ans.val();
    for (int i=1;i<N;i++){
        mint ans = seg.get(i);
        cout << " " << ans.val();
    }
}
//範囲がR-L+1の部分で(R-L)/(R-L+1)倍したうえでX*(R-L+1)を足す感じになるのか。