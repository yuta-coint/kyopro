#include <bits/stdc++.h>
using namespace std;
#define rep(i,n) for (int i = 0; i < (n); ++i)
#define rep2(i,k,n) for (int i = k; i < (n); ++i)
int main(){
    int t;cin>>t;
    for(int ca;ca<t;ca++){
        int w,d,h;cin >> w>> d >> h ;
        int a,b,f,g;cin >> a>> b >> f >> g;
        long long ans;
        long long ans1,ans2,ans3,ans4;
        ans1 = h+a+f+abs(b-g);
        ans2 = h+b+g+abs(a-f);
        ans3 = h+(w-a)+(w-f)+abs(b-g);
        ans4 = h+(d-b)+(d-g)+abs(a-f);
        ans = min({ans1,ans2,ans3,ans4});
        cout << ans << endl;
    }
}