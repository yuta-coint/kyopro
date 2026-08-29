#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;cin>>t;
    for (int ca=0;ca<t;ca++){
        int n,m;cin >>n>>m;
        set <int> three;
        int one=0;int two= 0;
        vector <int> check(m);
        for (int i=0;i<m;i++){
            check[i]=0;
        }
        for (int i=0;i<n;i++){
            int x;
            cin>>x;
            if (x==-1){
                one+=1;
            }else if(x==-2){
                two+=1;
            }else{
                check[x-1]=1;
            }
        }
        vector <int> fore(m);
        vector <int> back(m);
        int cnt = 0;
        for (int i=0;i<m;i++){
            fore[i]=cnt;
            cnt+=1-check[i];
        }
        cnt=0;
        for (int i=m-1;i>=0;i--){
            back[i]=cnt;
            cnt+=1-check[i];
        }
        int sck = count(check.begin(), check.end(),1);
        int ans = min(max(one,two),m-sck);
        for (int i=0;i<m;i++){
            if (check[i]==1){
                if (min(fore[i],one)+min(back[i],two)>ans){
                    ans = min(fore[i],one)+min(back[i],two);
                }
            }
        }
        //cout << ans << endl;
        cout << ans+sck << endl;
    }
}