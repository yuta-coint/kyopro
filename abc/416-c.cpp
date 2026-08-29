#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
int main(){
    vector<string> candidate;
    int N, K,X;
    cin >> N >> K >> X;
    vector<string> S(N);
    for (int i = 0; i < N; i++){
        cin >> S[i];
    }
    for (int i = 0; i< pow(N, K); i++){
        string tmp = "";
        for (int j = 0; j < K; j++){
            tmp += S[(i / int(pow(N, j))) % N];
        }
        candidate.push_back(tmp);
    }
    sort(candidate.begin(), candidate.end());
    cout << candidate[X - 1] << endl;
    return 0;
}