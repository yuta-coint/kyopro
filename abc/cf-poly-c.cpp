#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define rep2(i,k,n) for (int i = k; i < (n); ++i)
int main(){
    int t;cin>>t;
    for(int ca;ca<t;ca++){
        string ans="YES";
        int n;cin >> n;
        string s;
        cin >> s;
        vector<int> a(n-1);
        rep(i,n-1) {a[i]=int(s[i]-'0');}
        int l=0;
        int r = 0;
        rep(i,n-1) {
            if (a[i]==0){
                l=i+1;
            }else{
                r=i+1;
            }
            if (l==0 && r==0){continue;}
            if (l==0 || r==0){cout << 1 << " ";continue;}
            cout << min(l,r)+1 << " ";
        }
        cout << "" << endl;
    }
}