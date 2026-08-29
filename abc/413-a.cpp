#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
int main(){
    int M,N;
    cin >> N >> M;
    int ans = 0;
    int a;
    for (int i = 0; i < N ;++i){
        cin >> a;
        ans += a;
    }
    if (ans <= M){
        cout << "Yes" << endl;
    }else{
        cout << "No" << endl;
    }
}