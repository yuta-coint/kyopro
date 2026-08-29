#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using mint = modint998244353;
//「同じ文字であるか、P側が_」ならOK、っていう状況が難しいな。
//(x-y)yでconvolutionすればいい
int main(){
    int L,W;
    cin >> L >> W;
    string S0,P0;
    cin >> S0;
    cin >> P0;
    map<char,mint> hash;
    char alpha = 'a';
    for (int i=0;i<26;i++){
        hash[alpha]=rand() % 998244353;
        alpha++;
    }
    alpha = 'A';
    for (int i=0;i<26;i++){
        hash[alpha]=rand() % 998244353;
        alpha++;
    }
    hash['.']=rand()%998244353;
    hash['_']=0;
    vector<mint> S,P;
    for (int i=0;i<W-1;i++){
        S.push_back(hash['.']);
    }
    for (int i=0;i<L;i++){
        S.push_back(hash[S0[i]]);
    }
    for (int i=0;i<W-1;i++){
        S.push_back(hash['.']);
    }
    for (int i=0;i<W;i++){
        P.push_back(hash[P0[W-1-i]]);
    }
    vector<mint> SP;
    SP = convolution(S,P);
    vector<mint> pow2;
    //累積和を考えよう！
    mint acu = 0;
    for (int i=0;i<W;i++){
        acu+=P[i]*P[i];
    }
    int ans = 0;
    for (int i=W-1;i<L+2*W-2;i++){
        if (SP[i]==acu){
            ans+=1;
        }
    }
    cout << ans << endl;
}