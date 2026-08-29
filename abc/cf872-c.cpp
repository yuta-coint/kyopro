#include <bits/stdc++.h>
using namespace std;
using Graph = vector<vector<int>>;

// 深さ優先探索
vector<bool> seen;
vector <int> size_of_subtree={};
void dfs(const Graph &G, int v) {
    seen[v] = true; // v を訪問済にする

    // v から行ける各頂点 next_v について
    for (auto next_v : G[v]) { 
        if (seen[next_v]) continue; // next_v が探索済だったらスルー
        dfs(G, next_v); // 再帰的に探索
        size_of_subtree[v]+=size_of_subtree[next_v];
    }
}
long long modpow(long long a, long long n, long long mod) {
    long long res = 1;
    while (n > 0) {
        if (n & 1) res = res * a % mod;
        a = a * a % mod;
        n >>= 1;
    }
    return res;
}

int main() {
    // 頂点数と辺数
    int N, k; cin >> N >> k;
    int M = N-1;

    // グラフ入力受取 (ここでは無向グラフを想定)
    Graph G(N);
    for (int i = 0; i < M; ++i) {
        int a, b;
        cin >> a >> b;
        G[a-1].push_back(b-1);
        G[b-1].push_back(a-1);
    }
    long long ans = 0;
    for (int i = 0;i<N;i++){
        size_of_subtree.push_back(1);
    }
    // 頂点 0 をスタートとした探索
    seen.assign(N, false); // 全頂点を「未訪問」に初期化
    dfs(G, 0);
    long long mod = pow(10,9)+7;
    //int half = modpow(2,mod-2,mod);
    if (k==2){
        for (int i = 1;i<N;i++){
            ans+=size_of_subtree[i]*(N-size_of_subtree[i])%mod;
            ans%=mod;
        }
        long long mother = modpow(N*(N-1)/2,mod-2,mod);
        cout << (ans*mother+1)%mod << endl;
    }else{
        cout << 1 << endl;
    }
}