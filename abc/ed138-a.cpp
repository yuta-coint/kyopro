#include <bits/stdc++.h>
#include<math.h>
using namespace std;
int main(){
    int t;cin>>t;
    string ans;
    for(int ca;ca<t;ca++){
        ans = "Yes";
        int n,m;
        cin >> n >> m;
        vector <int> file(n);
        vector <int> rank(n);
        for (int rook;rook<m;rook++){
            cin >> x >> y;
        }
        for (int f; f<n;f++){
            if file[f]<3{ans="No";}
        }
        for (int r; r<n;r++){
            if rank[r]<3{ans="No";}
        }
    }
}