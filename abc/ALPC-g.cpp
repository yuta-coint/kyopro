#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using ll = long long;
int main(){
    int N,M;
    cin >> N >>M;
    scc_gragh graph(N);
    for (int i=0;i<M;i++){
        int a,b;
        cin >> a>>b;
        graph.add_edge(a,b);
    }
    vector<vector<int>> ans = graph.scc();
    for (int i=0;i<ans.size();i++){
        
    }
}
