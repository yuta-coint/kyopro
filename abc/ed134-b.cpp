#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;cin>>t;
    int n;int m;int sx;int sy;int d;int ans;
    for (int i=0;i<t;i++){
        cin >> n >> m >> sx >> sy >> d;
        ans = -1;
        if (sx-d>1 and sy+d<m){
                ans = m+n-2;
            }
        if (sy-d>1 and sx+d<n){
                ans = m+n-2;
            }
        cout << ans << endl;
    }
}
