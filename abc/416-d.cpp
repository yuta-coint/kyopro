#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
typedef long long ll;
ll solve(){
    int N,M;
    cin >> N >> M;
    vector<int> A(N);
    ll ans = 0;
    for (int i = 0; i < N; i++){
        cin >> A[i];
        ans += A[i];
    }
    vector<int> B(N);
    for (int i = 0; i < N; i++){
        cin >> B[i];
        ans += B[i];
    }
    sort(A.begin(), A.end());
    sort(B.begin(), B.end());
    int i = 0, j = N-1;
    while (i < N && j >= 0){
        if (A[i] + B[j] < M){
            i++;
        } else {
            i++;
            j--;
            ans -= M;
        }
    }
    return ans;
}
int main(){
    int T;
    cin >> T;
    while (T--){
        cout << solve() << endl;
    }
}