#include <bits/stdc++.h>
#include<math.h>
using namespace std;
int main(){
    int t;cin>>t;
    long long ans;
    for(int ca;ca<t;ca++){
        ans = 0;
        long long l;long long r;
        cin >> l >> r;
        long long temp = floor(sqrt(r));
        //cout << temp << endl;
        ans += (temp-1)*3;
        if(r>=temp*(temp+1)){
            ans+=1;
        }
        if(r>=temp*(temp+2)){
            ans+=1;
        }
        temp = floor(sqrt(l-1));
        ans -= (temp-1)*3;
        if(l-1>=temp*(temp+1)){
            ans-=1;
        }
        if(l-1>=temp*(temp+2)){
            ans-=1;
        }
        cout << ans <<endl;
    }
}