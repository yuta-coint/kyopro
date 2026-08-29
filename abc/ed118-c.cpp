#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;cin>>t;
    for(int i;i<t;i++){
        int n;long long h;
        cin >> n >> h;
        //cout << n << h << endl;
        vector <long long> a(n);
        for(int j=0;j<n;j++){
            cin >> a[j];
        }
        long long ok;long long ng;
        ok = h;
        ng = 0;
        long long med;
        while (ng+1<ok){
            long long doragon;doragon=0;
            med = (ng+ok)/2;
           // cout << med << endl;
            for (int j=0;j<n-1;j++){
                doragon+=min(a[j+1]-a[j],med);
            }
            doragon+=med;
            if (doragon>=h){
                ok=med;
            }else{
                ng=med;
            }
        }
        cout << ok << endl;
    }
}