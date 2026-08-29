#include <bits/stdc++.h>
#include <unordered_set>
using namespace std;
typedef long long ll;
int main(){
    int T;
    int N;
    cin >> T;
    for (int ca = 0; ca < T; ++ca){
        vector<ll> A;
        cin >> N;
        for (int i; i < N; ++i){
            ll a;
            cin >> a;
            A.push_back(a);
        }
        sort(A.begin(), A.end());
        int plus1,minus1,minus2;
        plus1=0;minus1 = 0;minus2 = 0;
        for (int i = 0; i< N-2; ++i){
            if (A[i]*A[i+2] != A[i+1] * A[i+1]){
                plus1 = 1;
            }
        }
        //負の公比にならないか
        for (int i = 0; 2*i < N-2; ++i){
            if (A[i]*A[i+1] != A[N-i-1]*A[N-i-1]){
                minus1 = 1;
            }
        }
        for (int i = 0; 2*i < N-3; ++i){
            if (A[N-i-1]*A[N-i-2] != A[i+1]*A[i+1]){
                minus1 = 1;
            }
        }
        for (int i = 0; 2*i < N-2; ++i){
            if (A[N-i-1]*A[N-i-2] != A[i]*A[i]){
                minus2 = 1;
            }
        }
        for (int i = 0;  2*i < N-3; ++i){
            if (A[i]*A[i+1] != A[N-i-2]*A[N-i-2]){
                minus2 = 1;
            }
        }
        if (plus1*minus1*minus2 == 0){
            cout << "Yes" << endl;
        }else{
            cout << "No" << endl;
        }
    }
}

s = [-10**9,10**9,10**6,3,5,1,9,6,-7]
for i in range(10):
    A = []
    A.append(s[i])
A.sort()