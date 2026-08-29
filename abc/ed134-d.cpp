#include <bits/stdc++.h>
using namespace std;
vector<int> compress(vector<int>A){
    // コピー
    vector<int> B = A;
    // B を小さい順にソート
    sort(B.begin(), B.end());
    // B から重複を除去する
    B.erase(unique(B.begin(), B.end()), B.end());
    // 座標圧縮した結果を求める
    vector<int> res(A.size());
    for (int i = 0; i < A.size(); ++i) {
        res[i] = lower_bound(B.begin(), B.end(), A[i]) - B.begin();
    }
    return res;
}
int main(){
    int t;cin>>t;
    for(int ca;ca<t;ca++){
        int n;cin >> n;
        vector <int> a(n);
        vector <int> b(n);
        vector <int> group_a(n);
        vector <int> group_b(n);
        for(int j=0;j<n;j++){
            cin >> a[j];
        }
        for(int j=0;j<n;j++){
            cin >> b[j];
        }
        int ans=0;
        for(int dig=29;dig>=0;dig--){            
            vector <int> bit_count(n,0);
            for(int i=0;i<n;i++){
                //各グループについて1の数を数える
                if((a[i]>>dig)&1){
                    bit_count[group_a[i]]+=1;
                }                
                if(((b[i]>>dig)&1)^1){
                    bit_count[group_b[i]]-=1;
                }
            }
            int flag=0;
            //for(int i=0;i<n;i++){cout << bit_count[i] << " ";}
            //cout << endl;
            for(int i=0;i<n;i++){
                if(bit_count[i]!=0){
                    flag=1;
                    break;
                }
            }
            if(flag==0){
                ans+=1<<dig;
                for(int j=0;j<n;j++){
                    group_a[j]*=2;
                    group_a[j]+=(a[j]>>dig)&1;
                }
                for(int j=0;j<n;j++){
                    group_b[j]*=2;
                    group_b[j]+=((b[j]>>dig)&1)^1;
                }
                group_a = compress(group_a);
                //for(int i=0;i<n;i++){cout << group_a[i] << " ";}
                //cout << endl;
                group_b = compress(group_b);
            }         
        }
        cout << ans << endl;
    }
}