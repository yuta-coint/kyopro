#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using ll = long long;
int main(){
    //N*MがスタートでN*M+1がゴール
    int N,M;
    cin >>N >>M;
    mf_graph<int> graph(N*M+2);
    vector<string> field = {};
    for (int i=0;i<N;i++){
        string s;
        cin >> s;
        field.push_back(s);
    }
    vector<pair<int,int>> edges = {};
    for (int i=0;i<N-1;i++){
        for (int j=0;j<M;j++){
            if (field[i][j]=='.' && field[i+1][j]=='.'){
                if ((i+j)&1){
                    graph.add_edge(i*M+j,(i+1)*M+j,1);
                }else{
                    graph.add_edge((i+1)*M+j,i*M+j,1);
                }
                edges.push_back(pair(i*M+j,(i+1)*M+j));
            }
        }
    }
    for (int i=0;i<N;i++){
        for (int j=0;j<M-1;j++){
            if (field[i][j]=='.' && field[i][j+1]=='.'){
                if ((i+j)&1){
                    graph.add_edge(i*M+j,i*M+j+1,1);
                }else{
                    graph.add_edge(j+1+i*M,j+i*M,1);
                }
                edges.push_back(pair(j+i*M,j+i*M+1));
            }
        }
    }
    for (int i=0;i<N;i++){
        for (int j=0;j<M;j++){
            if ((i+j)&1){
                graph.add_edge(N*M,j+i*M,1);
            }else{
                graph.add_edge(j+i*M,N*M+1,1);
            }
        }
    }
    cout << graph.flow(N*M,N*M+1) << endl;
    vector<char> ans(N*M);
    for (int i=0;i<N;i++){
        for (int j=0;j<M;j++){
            ans[i*M+j]=field[i][j];
        }
    }
    int es = edges.size();
    for (int i=0;i<es;i++){
        int check = graph.get_edge(i).flow;
        if (check==1){
            int s = edges[i].first;
            int t = edges[i].second;
            if (t-s!=M){
                ans[s]='>';
                ans[t]='<';
            }else{
                ans[s]='v';
                ans[t]='^';
            }
        }
    }
    for (int i=0;i<N;i++){
        for (int j=0;j<M;j++){
            cout << ans[i*M+j];
        }
        cout <<"" << endl;
    }
}