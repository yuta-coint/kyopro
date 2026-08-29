#include <bits/stdc++.h>
#include <string>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)
int main(){
    int t;cin>>t;
    for(int ca;ca<t;ca++){
        int n;cin >> n;
        string s;
        cin >> s;
        int cnt=0;
        rep(i,n) {if (int(s[i]-'0')==1)cnt++;}
        int temp = cnt/2;
        vector<string> ans(n-1);
        rep(i,n-1){
            //cout << i <<endl;
            if (int(s[i+1]-'0')==1 && temp>0){
                ans[i]="-";
                temp-=1;
            }else{
                ans[i]="+";
            }
        }
        rep(i,n-1){
            cout << ans[i];
        }
        cout<<"" << endl;
    }
}