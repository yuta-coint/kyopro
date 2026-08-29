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
int main(){
    //貼ると累乗とその逆数を出力できる///////////////
    long long mod;
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
    //print(fac_rev,10);
    /////////////////////////////////////////////////
    int N,M;
    cin >>N >> M;
    vector<long> count_a(11);
    for (int i=0;i<11;i++){
        count_a[i]=0;
    }
    for (int i=0;i<N;i++){
        long a;
        cin >> a;
        count_a[a]+=1;
    }
    vector<long> ans(M+1);
    vector<long> temp(M+1);
    vector<long> conv(2*M+1);
    for (int j=0;j<M+1;j++){
        ans[j]=0;
    }
    ans[0]=1;
    //iの倍数の項だけ残す
    for (int i=1;i<11;i++){
        for (int j=0;j<M+1;j++){
            if (j%i==0){
                int k;
                k=j/i;
                if (k>count_a[i]){
                    temp[j]=0;
                }else{
                    //count_a[i]Ck
                    temp[j]=fac_rev[k]*fac_rev[count_a[i]-k]%mod*fac[count_a[i]]%mod;
                }
            }else{
                temp[j]=0;
            }
        }
        conv = convolution<998244353>(ans,temp);
        for (int j=0;j<M+1;j++){
            ans[j]=conv[j];
        }

    }
    //print(ans,M+1);
    vector<long> ans2(M+1);
    for (int j=0;j<M+1;j++){
        ans2[j]=0;
    }
    ans2[0]=1;
    for (int i=1;i<11;i++){
        for (int j=0;j<M+1;j++){
            if (j%i==0){
                int k;
                k=j/i;
                if (k>count_a[i]){
                    temp[j]=0;
                }else{
                    //count_a[i]Ck
                    temp[j]=fac_rev[k]*fac_rev[count_a[i]-k]%mod*fac[count_a[i]]%mod;
                }
                if (k&1==1){
                    temp[j]=(mod-temp[j])%mod;
                }
            }else{
                temp[j]=0;
            }
        }
        conv = convolution<998244353>(ans2,temp);
        for (int j=0;j<M+1;j++){
            ans2[j]=conv[j];
        }
    }
    cout <<(998244353+ans[M]-ans2[M])*499122177%998244353 << endl;
}