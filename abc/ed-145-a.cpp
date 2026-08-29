#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define rep2(i,k,n) for (int i = k; i < (n); ++i)
int main(){
    int t;cin>>t;
    for(int ca;ca<t;ca++){
        string s;
        cin >> s;
        vector<int> a(10);
        for (int i=0;i<4;++i){
            a[s[i]-'0']+=1;
        }
        if (count(a.begin(), a.end(), 4) > 0){
            cout << -1 << endl;
        }else if (count(a.begin(),a.end(),3)>0) {
            cout << 6 << endl;
        }else{
            cout << 4 << endl;
        }
    }
}
