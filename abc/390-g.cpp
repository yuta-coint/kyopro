#include <iostream>
#include <vector>
#include <set>
#include <atcoder/modint>
#include <atcoder/convolution>
#include <cmath>
using namespace std;
using namespace atcoder;
using mint = modint998244353;
int main() {
    int N;
    cin >> N;
    vector<int> keta(6);
    int temp;
    for (int i = 0; i < 6; i++){
        if (N >= pow(10,i+1)-1){
            keta[i] = pow(10,i+1)-pow(10,i)-1;
        }else if(N >= pow(10,i)){
            keta[i] = N - pow(10,i);
        }else{
            keta[i] = 0;
        }
    }

    vector<mint> fac(7*N);
    mint r = 1;
    fac[0]=r;
    for (int i = 1; i < N*7; i++) {
        r = r*i;
        fac[i] = r;
    }
    

    r = r.inv();
    vector<mint> fac_inv(7*N);
    fac_inv[7*N-1]=r;
    for (int i = 7*N-1; i>=1; i--){
        r = r*i;
        fac_inv[i-1] = r;
    }
    //cout << keta[0] << endl;

    vector<mint> A(N);
    mint ten_pow = 1;
    for (int j = 0; j < N; j++) {
        if (j>keta[0]){
            A[j] = 0;
        }else{
            A[j] = ten_pow*fac[keta[0]]*fac_inv[j]*fac_inv[keta[0]-j];
        }
        ten_pow *= 10;
    }

    vector<mint> B(N);
    mint pw = 10;
    for (int i=1;i<6;i++){
        pw = pw*10;
        ten_pow = 1;
        for (int j = 0; j < N; j++){
            if (j>keta[i]){
                B[j]=0;
            }else{
                B[j]=ten_pow*fac[keta[i]]*fac_inv[j]*fac_inv[keta[i]-j];
            }
            ten_pow = ten_pow*pw;
        }
        //畳み込む
        A = convolution<mint>(A,B);
    }
    
    //cout << A[0].val() << endl;
    //cout << A[1].val() << endl;

    vector<mint> C(N);
    mint ans;
    vector<mint> kc(6);
    int kc_sum;
    for (int i=0;i<6;i++){
        C = A;
        for (int j = 1; j < N+1; j++){
            if (pow(10,i)<=j && j<pow(10,i+1)){
                kc[i]= kc[i]+j;
                kc_sum = kc_sum+i+1;
            }
        }
    //cout << kc[0].val() << endl;
    //cout << kc[1].val() << endl;
    
        mint ten = 10;
        for (int l=0;l<6;l++){
            if(i==l){
                continue;
            }
            if (N<pow(10,l)){
                continue;
            }
            for (int j = N-1; j > 0; j--){
                C[j] = C[j]+C[j-1]*(ten.pow(l+1));
            }
        }
        for (int j = 0; j < N; j++){
            ans =  ans + kc[i]*C[j]*fac[j]*fac[N-j-1];
        }
        //cout << ans.val() << endl;
    }
    cout << ans.val() << endl;

    return 0;
}

