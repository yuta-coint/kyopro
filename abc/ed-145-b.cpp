#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;cin>>t;
    for(int ca;ca<t;ca++){
        long long n;cin>>n;
        if (n==1){
            cout << 0 << endl;
            continue;
        }
        long long temp = sqrt(n-1);
        cout << temp <<endl;
    }
}