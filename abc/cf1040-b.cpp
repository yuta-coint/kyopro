#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int solve(){
    int N,S;
    cin >> N >> S;
    int z,p,t;
    z = 0;
    p = 0;
    t = 0;
    int wa = 0;
    for (int i = 0; i < N; i++){
        int x;
        cin >> x;
        if (x == 0){
            z+=1;
        }else if (x == 1){
            //cout << "i" << endl;
            p+=1;
        }else{
            t+=1;
        }
        wa += x;
    }
    //cout << "z: " << z << ", p: " << p << ", t: " << t << endl;
    if (wa > S || wa + 1 == S){
        for (int i = 0; i < z; i++){
            cout << 0 << " ";
        }
        for (int i = 0; i < t; i++){
            cout << 2 << " ";
        }
        for (int i = 0; i < p-1; i++){
            cout << 1 << " ";
        }
        cout << 1 << endl;
        return 0;
    }else{
        cout << -1 << endl;
        return 0;
    }
}
int main(){
    int T;
    cin >> T;
    for (int i = 0; i < T; i++){
        solve();
    }
    return 0;
}