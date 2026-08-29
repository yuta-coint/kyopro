#include <bits/stdc++.h>
using namespace std;
int main(){
    int t;cin>>t;
    bool ans;
    for(int ca;ca<t;ca++){
        int n;
        cin >> n;
        int r1,r2,r3;
        int c1,c2,c3;
        cin >> r1 >> c1>> r2 >> c2 >> r3 >> c3;
        int x;int y;
        if(r1==r2 or r1==r3){
            x = r1;
        }else{
            x = r2;
        }
        if(c1==c2 or c1==c3){
            y = c1;
        }else{
            y = c2;
        }
        int gx,gy;
        cin >> gx >> gy;
        ans = false;
        if(((gx-x)&1) and ((gy-y)&1)){
            ans = false;
        }else if((x==1 or x==n) and (y==1 or y==n)){
            if((gx==x) or (gy==y)){
                ans=true;
            }
        //}else if(x==1){
        //    if((gx==x) or (gy==y) or (gx+gy==x+y+1)or(gy-gx==y-x-1)){
                ans=true;
            }
        }else if(x==n){
            if((gx==x) or (gy==y) or (gx+gy==x+y+1)or(gy-gx==y-x+1)){
                ans=true;
            }
        }else if(y==1){
            if((gx==x) or (gy==y) or (gx+gy==x+y-1)or(gy-gx==y-x+1)){
                ans=true;
            }
        }else if(y==n){
            if((gx==x) or (gy==y) or (gx+gy==x+y-1)or(gy-gx==y-x-1)){
                ans=true;
            }
        }else{
            ans = true;
        }
        if(ans){
            cout << "YES" << endl;
        }else{
            cout << "NO" << endl;
        }
    }
}