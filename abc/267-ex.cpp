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
    vector<long> ans(n+1,0);
    ans[0]=1;
    if (k==0){
        return(ans);
    }
    int cnt = 0;
    while (cnt<30){
        cnt+=1;
        long cnt_pow;
        cnt_pow = 1<<cnt;
        if (cnt_pow>k){
            break;
        }
    }
    //print(ans,N+1);
    vector<long> temp;
    for (int i=cnt;i>=0;i--){
        temp = convolution<998244353>(ans,ans);
        ans = temp;
        if ((k>>i)&1==1){
            temp = convolution<998244353>(ans,a);
            ans = temp;
            //print(ans,N+1);
        }
    }
    return(ans);
}
int main(){
    //int mod = 998244353;
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
    vector<long> ans(M+1,0);
    vector<long> temp(M+1);
    vector<long> temp_pow(M+1);
    ans[0]=1;
    for (int i=1;i<11;i++){
        for (int j=0;j<M+1;j++){
            temp[j]=0;
        }
        temp[0]=1;
        if (i<=M){
            temp[i]=1;
        }
        temp_pow = poly_pow(temp,M,count_a[i]);
        ans = convolution<998244353>(ans,temp_pow);
    }
    //print(ans,M+1);
    vector<long> ans2(M+1,0);
    ans2[0]=1;
    for (int i=1;i<11;i++){
        for (int j=0;j<M+1;j++){
            temp[j]=0;
        }
        temp[0]=1;
        if (i<=M){
            temp[i]=998244352;
        }
        temp_pow = poly_pow(temp,M,count_a[i]);
        ans2 = convolution<998244353>(ans2,temp_pow);
    }
    cout <<(998244353+ans[M]-ans2[M])*499122177%998244353 << endl;
}