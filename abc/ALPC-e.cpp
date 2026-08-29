#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using ll = long long;
int main(){
    //N*MがスタートでN*M+1がゴール
    int N,K;
    cin >>N>>K;
    mcf_graph<ll,ll> graph(N+N+2);
    for (int i=0;i<N;i++){
        for (int j=0;j<N;j++){
            ll A;
            cin >> A;
            graph.add_edge(i+1,N+j+1,1,pow(10,9)-A);
        }
    }
    for (int i=0;i<N;i++){
        graph.add_edge(0,i+1,K,0);
    }
    for (int i=0;i<N;i++){
        graph.add_edge(N+i+1,N+N+1,K,0);
    }
    graph.add_edge(0,N+N+1,N*N,pow(10,9));
    pair<ll,ll> flmc;
    flmc = graph.flow(0,N+N+1,N*N);
    ll ans = N*N*(pow(10,9))-flmc.second;
    cout << ans << endl;
    for (int i=0;i<N;i++){
        for (int j=0;j<N;j++){
            auto cond = graph.get_edge(i*N+j);
            if (cond.flow ==1){
                cout << "X";
            }else{
                cout << ".";
            }
        }
        cout << "" << endl;
    }
}