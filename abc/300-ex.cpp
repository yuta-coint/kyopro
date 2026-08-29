#include <iostream>
#include <vector>
#include <algorithm>
#include <math.h>
#include <atcoder/convolution>
#include <atcoder/modint>

using namespace std;
using namespace atcoder;

using mint = modint998244353;
mint Bostan_Mori(const vector<mint>& P, const vector<mint>& Q, long long N) {
    if (N == 0){
        return P[0] / Q[0];
    }
    vector<mint> Q_minus = Q;
    for (int i = 1; i < (int)Q_minus.size(); i += 2){
        Q_minus[i] = -Q_minus[i];
    }
    vector<mint> P_new, Q_new;
    P_new = convolution(P, Q_minus);
    Q_new = convolution(Q, Q_minus);
    vector<mint> P_next, Q_next;
    if (N % 2 == 0){
        for (int i = 0; i < (int)P_new.size(); i += 2){
            P_next.push_back(P_new[i]);
        }
    }else{
        for (int i = 1; i < (int)P_new.size(); i += 2){
            P_next.push_back(P_new[i]);
        }
    }
    for (int i = 0; i < (int)Q_new.size(); i += 2){
        Q_next.push_back(Q_new[i]);
    }
    return Bostan_Mori(P_next, Q_next, N / 2);
}


mint Bostan_Mori_Sum(const vector<mint>& P, const vector<mint>& Q, long long N) {
    if (N == 0){
        return P[0] / Q[0];
    }
    vector<mint> Q_minus = Q;
    for (int i = 1; i < (int)Q_minus.size(); i += 2){
        Q_minus[i] = -Q_minus[i];
    }
    vector<mint> P_new, Q_new;
    P_new = convolution(P, Q_minus);
    Q_new = convolution(Q, Q_minus);
    vector<mint> P_next;
    if (N % 2 == 0){
        for (int i = 0; i < (int)P_new.size(); i += 2){
            P_next.push_back(P_new[i]);
        }
    }else{
        int L = (int)P_new.size();
        L = (L + 1) / 2;
        P_next = vector<mint>(L, 0);
        for (int i = 0; i < (int)P_new.size(); i++){
            P_next[i / 2] += P_new[i];
        }
    }
    vector<mint> Q_next;
    for (int i = 0; i < (int)Q_new.size(); i += 2){
        Q_next.push_back(Q_new[i]);
    }
    return Bostan_Mori_Sum(P_next, Q_next, N / 2);
}

int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int K;
    long long N;
    cin >> K >> N;
    vector<mint> start(K , 1);
    vector<mint> relation_ships(K + 1, -1);
    relation_ships[0] = 1;
    vector<mint> g = convolution(start, relation_ships);
    g.resize(K);
    cout << Bostan_Mori_Sum(g, relation_ships, N).val() << "\n";
}


int main(){
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    int K;
    long long N;
    cin >> K >> N;
    vector<mint> start(K , 1);
    vector<mint> relation_ships(K + 1, -1);
    relation_ships[0] = 1;
    vector<mint> g = convolution(start, relation_ships);
    g.resize(K);
    cout << Bostan_Mori(g, relation_ships, N - 1).val() << "\n";
}