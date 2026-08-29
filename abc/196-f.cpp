#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
int main(){
    string S0,T0;
    cin >> S0;
    cin >> T0;
    int lens,lent;
    lens=S0.size();
    lent=T0.size();
    vector<int> S,T;
    for (int i=0;i<lens;i++){
        int k;
        k = int(S0[i]-'0');
        S.push_back(k);
    }
    for (int i=0;i<lent;i++){
        int k;
        k = int(T0[lent-i-1]-'0');
        T.push_back(k);
    }
    vector<int> ST;
    //1が被っている個数を確認する
    ST = convolution(S,T);
    for (int i=0;i<lens;i++){
        S[i]=1-S[i];
    }
    for (int i=0;i<lent;i++){
        T[i]=1-T[i];
    }
    vector<int> ST2;
    //0が被っている個数を確認する
    ST2 = convolution(S,T);
    int ans = 0;
    for (int i=lent-1;i<lens;i++){
        ans = max(ST[i]+ST2[i],ans);
    }
    cout << lent-ans << endl;
}