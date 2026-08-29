#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;cin>>t;
    for(int ca;ca<t;ca++){
        int n,k;cin>>n>>k;
        k = n*(n+1)/2 - k;
        vector<int> cnt{};
        //転倒数がkの数列を構築する
        for (int i=0;i<n+1;i++){
            if (k>=n-i){
                cnt.push_back(n-i);
                k-=n-i;
            }else{
                cnt.push_back(k);
                for (int j=0;j<n-i+1;j++){
                    if (j!=k){
                        cnt.push_back(j);
                    }
                }
                break;
            }
            //cout << cnt.size()<<endl;
        }
        for (int i=0;i<n-1;i++){
            cout << cnt[i+1]-cnt[i] << " ";
        }
        cout << cnt[n]-cnt[n-1] <<endl;
    }
}