#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using mint = modint998244353;
struct Node {
    mint a, b, c;
    Node(mint a = 0, mint b = 0, mint c = 0) : a(a), b(b), c(c) {}
};
//和、二乗和、長さ
Node e(){
    Node r = {0,0,0};
    return r;
}

Node op(Node u,Node v){
    Node r = {0,0,0};
    r.a = u.a+v.a;
    r.b = u.b+v.b;
    r.c = u.c+v.c;
    return r;
}

Node mapping(mint f,Node x){
    return {x.a + f * x.c, x.b + 2 * f * x.a + f * f * x.c, x.c};
}

mint composition(mint f,mint g){
    return f+g;
}

mint id(){
    return 0;
}

int main(){
    int N,Q;
    cin >> N >> Q;
    vector<Node> start(N + 1);
    for (int i=0;i<N+1;i++){
        start[i] = {0,0,1};
    }
    lazy_segtree<Node, op, e, mint, mapping, composition, id> seg(start);
    for (int i = 0; i < Q; i++){
        int l, r;
        long long a_val;
        cin >> l >> r >> a_val;
        mint a = a_val;
        r += 1;
        seg.apply(l, r, a);
        Node ans = seg.prod(l, r);
        mint ans2 = (ans.a * ans.a - ans.b) * 499122177;
        cout << ans2.val() << endl;
    }
}