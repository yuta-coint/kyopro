#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using mint = modint998244353;
// a^n mod を計算する
long long modpow(long long a, long long n, long long mod) {
    long long res = 1;
    while (n > 0) {
        if (n & 1) res = res * a % mod;
        a = a * a % mod;
        n >>= 1;
    }
    return res;
}
//ベクトルを出力するのに使う
int print(vector<long> a,int n){
    for (int i=0;i<n-1;i++){
        cout << a[i]<<" ";
    }
    cout << a[n-1]<<endl;
    return 0;
}
//n次多項式a(n+1)をk乗する
vector<long> poly_pow(vector<long> a,int n,int k){
    //logn回畳み込む
    vector<long> ans(n+1);
    ans[0]=1;
    for (int i=1;i<n+1;i++){
        ans[i]=0;
    }
    //print(ans,N+1);
    vector<long> temp;
    for (int i=30;i>=0;i--){
        temp = convolution<998244353>(ans,ans);
        for (int j=0;j<n+1;j++){
            ans[j]=temp[j];
        }
        if ((k>>i)&1==1){
            temp = convolution<998244353>(ans,a);
            for (int j=0;j<n+1;j++){
                ans[j]=temp[j];
            }
            //print(ans,N+1);
        }
    }
    return(ans);
}
int main(){
    //貼ると累乗とその逆数を出力できる///////////////
    int mod;
    mod = 998244353;
    int big;
    big = 1000001;
    vector<long> fac(big),fac_rev(big);
    fac[0]=1;
    for (int i=1;i<big;i++){
        fac[i]=fac[i-1]*i%mod;
    }
    fac_rev[big-1]=modpow(fac[big-1],mod-2,mod);
    for (int i=big-1;i>0;i--){
        fac_rev[i-1]=fac_rev[i]*i%mod;
    }
    /////////////////////////////////////////////////
    int N,K;
    cin >> N >> K;
    vector<long> S(N+1);
    int s0;
    cin>>s0;
    if (s0>1){
        cout << 0 << endl;
        exit(0);
    }
    S[0]=1;
    for (int i=1;i<N+1;i++){
        S[i]=0;
    }
    for (int i=1;i<K;i++){
        int si;
        cin >> si;
        S[si-1]=fac_rev[si-1];
    }
    //logn回畳み込む
    vector<long> ans(N+1);
    ans=poly_pow(S,N,N);
    cout << ans[N-2]*fac[N-2]%mod << endl;
}