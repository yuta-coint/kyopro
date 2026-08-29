#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define rep2(i,k,n) for (int i = k; i < (n); ++i)
int main(){
    int t;cin>>t;
    for(int ca;ca<t;ca++){
        string ans="YES";
        priority_queue<int> que;
        int n,m,k,temp;cin >> n>>m>>k;
        rep(i,m) {cin >> temp;que.push(temp);}
        queue<int> stock;
        if (m<k){cout << "NO" << endl;continue;}
        rep(i,k) {
            //cout << que.top()-1 <<endl;
            stock.push(que.top()-1);
            que.pop();
        }
        rep2(i,k,n){
            //cout << que.top()-1 <<endl;
            que.push(stock.front());
            stock.pop();
            if (que.top()==0){ans="NO";}
            stock.push(que.top()-1);
            que.pop();
        }
        cout << ans << endl;
    }
}
#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define rep2(i,k,n) for (int i = k; i < (n); ++i)
int main(){
    int t;cin>>t;
    for(int ca;ca<t;ca++){
        string ans="YES";
        int n,m,k,temp;cin >> n>>m>>k;
        vector<int> a(m);
        rep(i,m) {cin >> a[i];}
        int cnt = 0;
        int ma = n/k;
        int plus_1 = n%k;
        rep(i,m) {
            if (a[i]==ma+1) {cnt++;}
            else if(a[i]>ma+1){ans = "NO";}
        }
        if (cnt>plus_1){ans = "NO";}
        cout << ans << endl;
    }
}