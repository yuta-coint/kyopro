#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using ll = long long;
int main(){
    //N*MがスタートでN*M+1がゴール
    int H,W,N;
    cin >>H >>W>>N;
    //白くするのにかかるコスト
    mcf_graph<ll,ll> graph(H+W+2);
    vector<ll> white1(H);
    vector<ll> white2(W);
    for (int i=0;i<H;i++){
        white1[i]=0;
    }
    for (int i=0;i<W;i++){
        white2[i]=0;
    }
    ll black = 0;
    for (int i=0;i<N;i++){
        ll A,B,C;
        cin >> A >> B >> C;
        black+=C;
        graph.add_edge(A,H+B,1,pow(10,9)-C);
        white1[A-1]+=1;
        white2[B-1]+=1;
    }
    for (int i=0;i<H;i++){
        graph.add_edge(0,i+1,white1[i]-1,0);
    }
    for (int i=0;i<W;i++){
        graph.add_edge(i+H+1,H+W+1,white2[i]-1,0);
    }
    graph.add_edge(0,H+W+1,H*W,pow(10,9));
    pair<ll,ll> flmc;
    flmc = graph.flow(0,H+W+1,H*W);
    ll ans = black-H*W*pow(10,9)+flmc.second;
    cout << ans << endl;
}