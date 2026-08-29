#include <bits/stdc++.h>
using namespace std;
int main() {
    int N;
    long long L = 0;
    vector<char> ans;
    cin >> N;
    for (int i = 0; i < N; i++) {
        char c;
        long long l;
        cin >> c >> l;
        if (L+l > 100){
            cout << "Too Long" << endl;
            return 0;
        }
        L += l;
        for (int j = 0; j < l; j++) {
            ans.push_back(c);
        }
    }
    for (char c : ans) {
        cout << c;
    }
}