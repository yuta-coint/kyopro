#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
//上から順に、0の長さの最大1の長さの最大、左端から測った0、左端から測った1,長さ
vector<long> e(){
    vector<long> r = {0,0,0,0,0,0,0};
    return r;
}

vector<long> op(vector<long> u,vector<long> v){
    vector<long> r(7);
    //0
    if (u[0]>v[0]){
        r[0]=u[0];
    }else{
        r[0]=v[0];
    }
    if (u[4]+v[2]>r[0]){
        r[0] = u[4]+v[2];
    }
    //1
    if (u[1]>v[1]){
        r[1]=u[1];
    }else{
        r[1]=v[1];
    }
    if (u[5]+v[3]>r[1]){
        r[1] = u[5]+v[3];
    }
    //2
    if (u[2]==u[6]){
        r[2] = u[2]+v[2];
    }else{
        r[2] = u[2];
    }
    if (u[3]==u[6]){
        r[3] = u[3]+v[3];
    }else{
        r[3] = u[3];
    }
    if (v[4]==v[6]){
        r[4] = u[4]+v[4];
    }else{
        r[4] = v[4];
    }
    if (v[5]==v[6]){
        r[5] = u[5]+v[5];
    }else{
        r[5] = v[5];
    }
    r[6] = u[6]+v[6];
    return r;
}

vector<long> mapping(int f,vector<long> x){
    if (f==0){
        return x;
    }else{
        return {x[1],x[0],x[3],x[2],x[5],x[4],x[6]};
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
    string S;cin>>S;
    vector<long> temp(7);
    vector<vector<long>> start(N);
    for (int i=0;i<N;i++){
        if (S[i]=='0'){
            start[i] = {1,0,1,0,1,0,1};
        }else{
            start[i] = {0,1,0,1,0,1,1};
        }
    }
    lazy_segtree<vector<long>, op, e, int, mapping, composition, id> seg(start);
    vector <long> ans(7);
    for (int q=0;q<Q;q++){
        int c,L,R;
        cin >> c>> L >> R;
        if (c==1){
            seg.apply(L-1,R,1);
        }else{
            ans = seg.prod(L-1,R);
            cout << ans[1] << endl;
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