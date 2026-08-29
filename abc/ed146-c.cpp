#include <bits/stdc++.h>
using namespace std;
using ll = long long;
int main(){
    int t;cin>>t;
    for (int ca=0;ca<t;ca++){
        int n;int s1; int s2;
        cin >> n >> s1 >> s2;
        vector<ll> r = {};
        int ri;
        for (int i=0;i<n;i++){
            cin >> ri;
            r.push_back(ri*pow(10,8)+i+1);
        }
        //for (int i=0;i<r.size();++i) cout << r[i]%(pow(10,8)) << " ";
        sort(r.begin(),r.end(),greater<ll>());
        int count1=1;int count2=1;
        vector<ll> a = {};
        vector<ll> b = {};
        ll pow18 = pow(10,8);
        for (int i=0;i<n;i++){
            if (count1*s1<count2*s2){
                a.push_back(r[i]%pow18);
                count1+=1;
            }else{
                b.push_back(r[i]%pow18);
                count2+=1;
            }
        }
        cout << a.size() << " ";
        for (int i=0;i<a.size();++i) cout << a[i] << " ";
        cout << endl;
        cout << b.size() << " ";
        for (int it:b) cout << it << " ";
        cout << endl;
    }
}