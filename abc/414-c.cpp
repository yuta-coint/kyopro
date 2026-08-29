#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
bool isPalindrome(ll N,int A){
    vector<int> v;
    while (N > 0){
        v.push_back(N % A);
        N /= A;
    }
    vector<int> v_reverse = v;
    reverse(v_reverse.begin(), v_reverse.end());
    if (v_reverse == v) {
        return true;
    }else{
        return false;
    }
}
int main() {
    int A;
    ll N;
    cin >> A;
    cin >> N;
    ll ans = 0;
    for (int i = 1; i < pow(10, 6); i++) {
        vector<int> B;
        vector<int> C;
        ll temp = i;
        while (temp > 0){
            B.push_back(temp % 10);
            temp /= 10;
        }
        ll chk = 0;
        C = B;
        reverse(B.begin(),B.end());
        B.insert(B.end(),C.begin(), C.end());
        for (int j = 0; j < B.size(); j++) {
            chk += B[j] * pow(10, j);
        }
        if (chk > N) {
            continue;
        }
        if (isPalindrome(chk, A)) {
            ans += chk;
            //cout << chk << endl;
        }
    }
    for (int i = 1; i < pow(10, 6); i++) {
        vector<int> B;
        vector<int> C;
        ll temp = i;
        while (temp > 0){
            if (temp != i){
                C.push_back(temp % 10);
            }
            B.push_back(temp % 10);
            temp /= 10;
        }
        ll chk = 0;
        reverse(B.begin(),B.end());
        B.insert(B.end(),C.begin(), C.end());
        for (int j = 0; j < B.size(); j++) {
            chk += B[j] * pow(10, j);
        }
        if (chk > N) {
            continue;
        }
        if (isPalindrome(chk, A)) {
            ans += chk;
            //cout << chk << endl;
        }
    }
    cout << ans << endl;
}