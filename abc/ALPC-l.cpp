#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
//0の数、1の数、転倒数
vector<long> e(){
    vector<long> r = {0,0,0};
    return r;
}

vector<long> op(vector<long> u,vector<long> v){
    vector<long> r(3);
    r[0] = u[0]+v[0];
    r[1] = u[1]+v[1];
    r[2] = u[2]+v[2]+u[1]*v[0];
    return r;
}

vector<long> mapping(int f,vector<long> x){
    if (f==0){
        return x;
    }else{
        return {x[1],x[0],x[0]*x[1]-x[2]};
    }
}

int composition(int f,int g){
    return f^g;
}

int id(){
    return 0;
}

int main(){
    int N,Q;
    cin >> N >> Q;
    vector<long> temp(3);
    vector<vector<long>> start(N);
    for (int i=0;i<N;i++){
        int Ai;
        cin >> Ai;
        if (Ai == 0){
            start[i] = {1,0,0};
        }else{
            start[i] = {0,1,0};
        }
    }
    lazy_segtree<vector<long>, op, e, int, mapping, composition, id> seg(start);
    vector <long> ans(3);
    for (int q=0;q<Q;q++){
        int T,L,R;
        cin >> T>> L >> R;
        if (T==1){
            seg.apply(L-1,R,1);
        }else{
            ans = seg.prod(L-1,R);
            cout << ans[2] << endl;
        }
        //for (int i=0;i<N;i++){
        //    for (int j=0;j<6;j++){
        //        cout << seg.get(i)[j];
        //    }
        //    cout << seg.get(i)[6] << endl;
        //}
    }
}


        //for (int i=0;i<N;i++){
            for (int j=0;j<6;j++){
                cout << seg.prod(1,3)[j];
            }
            cout << seg.prod(1,3)[6] << endl;
        //}