#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;cin>>t;
    for(int ca;ca<t;ca++){
        int n;cin >> n;
        vector <int> a(n);
        vector <int> ans_min(n);
        vector <int> ans_max(n);
        vector <int> b(n);
        for(int j=0;j<n;j++){
            cin >> a[j];
        }
        for(int j=0;j<n;j++){
            cin >> b[j];
        }
        int temp;temp=0;
        //b[temp]を引き受けられるかどうか
        for(int j=0;j<n;j++){
            while(temp<n){
                if (a[j]<=b[temp]){
                    ans_min[j]=b[temp]-a[j];
                    break;
                }
                temp++;
            }
        }
        //一つ下を引き受けられるか
        vector <bool> one_under(n,false);
        for(int j=1;j<n;j++){
            if (a[j]<=b[j-1]){
                one_under[j]=true;
            }
        }
        int win = n;
        for(int j=n-1;j>=0;j--){
            ans_max[j]=b[win-1]-a[j];
            if (one_under[j]==false){
                win = j;
            }
        }
        for (int i=0; i<n;i++) {
            cout << ans_min[i] << " ";
        }
        cout << endl;
        for (int i=0; i<n;i++) {
            cout << ans_max[i] << " ";
        }
        cout << endl;
    }
}