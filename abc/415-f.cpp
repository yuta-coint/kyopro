#include <bits/stdc++.h>
#include <atcoder/lazysegtree>
using namespace std;
using namespace atcoder;
typedef long long ll;
int e(){
    return 0;
}
int op(int a, int b){
    return a + b;
}
int ma(int a, int b){
    return max(a, b);
}
int mapping(int a, int b){
    return a + b;
}
int composition(int a, int b){
    return a + b;
}
int id(){
    return 0;
}
int main(){
    int N, Q;
    cin >> N >> Q;
    //その文字のlefter boundを求める。
    lazy_segtree<int, op, e, int, mapping, composition, id> Left(N);
    //その文字のrighter boundを求める。
    lazy_segtree<int, op, e, int, mapping, composition, id> Right(N);
    lazy_segtree<int, ma, e, int, mapping, composition, id> Lazy(N);
    string S;
    cin >> S;
    S = S + "1"; //番兵を追加
    char p = "1";
    int cnt = 0;
    for (int i = 0; i < N; i++){
        if (S[i] == p){
            Left.set(i, cnt);
        } else {
            p = S[i];
            cnt = i;
            Left.set(i, cnt);
        }
    }
    p = "1";
    cnt = N - 1;
    for (int i = N - 1; i >= 0; i--){
        if (S[i] == p){
            Right.set(i, cnt);
        } else {
            p = S[i];
            cnt = i;
            Right.set(i, cnt);
        }
    }
    for (int i = 0; i < N; i++){
        Lazy.set(i, Right.get(i) - Left.get(i));
    }
    for (int _ = 0; _ < Q; _++){
        int type;
        cin >> type;
        if (type == 1){
            int i;
            char x;
            cin >> i >> x;
            i--;
            if (S[i] == x) continue;
            //もとの状態から架空の文字列を抜き取る。
            if (i > 0 && S[i] == S[i-1]){
                //S[i-1]のrightが被害を受ける。
                Left.set(i, i);
                Lazy.set(i, Right.get(i) - Left.get(i));
                int dif;
                dif = (i-1) - Right.get(i-1);
                Right.apply(Right.get(i-1), i, dif);
                Lazy.apply(Left.get(i-1), i, dif);
            }
            if (i < N - 1 && S[i] == S[i+1]){
                //S[i+1]のleftが被害を受ける。
                Right.set(i, i);
                Lazy.set(i, Right.get(i) - Left.get(i));
                int dif;
                dif = (i+1) - Left.get(i+1);
                Left.apply(i + 1, Right.get(i + 1) + 1, - dif);
                Lazy.apply(i + 1, Right.get(i + 1) + 1, dif);
            }
            S[i] = x;
            //結果孤立しなかった場合
            if (i > 0 && S[i] == S[i-1]){
                //S[i-1]のrightが被害を受ける。
                Left.set(i, Left.get(i-1));
                Lazy.set(i, Right.get(i) - Left.get(i));
                int dif;
                dif = Right.get(i) - (i - 1);
                Right.apply(Left.get(i-1), i, dif);
                Lazy.apply(Left.get(i-1), i, dif);
            }
            if (i < N - 1 && S[i] == S[i+1]){
                //S[i+1]のleftが被害を受ける。
                Right.set(i, Right.get(i+1));
                Lazy.set(i, Right.get(i) - Left.get(i));
                int dif;
                dif = (i + 1) - Left.get(i + 1);
                Left.apply(i + 1, Right.get(i + 1) + 1, dif);
                Lazy.apply(i + 1, Right.get(i + 1) + 1, dif);
            }
        }else{
            int l,r;
            cin >> l >> r;
            l--; r--;
            int ans;
            int L,R;
            L = Right.get(l)+1;
            R = Left.get(r)-1;
            //全部同じ文字のとき
            if (L > r){
                ans = (r-l+1);
            }else{
                ans = min(r - R, L - l);
            }
            //三区間以上あるとき
            if (L < R){
                int tmp = Lazy.prod(L, R + 1);
                if (tmp > ans){
                    ans = tmp;
                }
            }
            cout << ans << endl;
        }
    }
}