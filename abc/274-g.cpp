#include <bits/stdc++.h>
using namespace std;
#include <atcoder/all>
using namespace atcoder;
using ll = long long;
int main(){
    int H,W;
    cin >> H >>W;
    mf_graph<int> graph(H*W*2+2);
    vector<string> S={};
    string s;
    for (int i;i<H;i++){
        cin >>s;
        S.push_back(s);
    }
    for (int i=0;i<H;i++){
        for (int j=0;j<W;j++){
            if (S[i][j]=='#'){continue;}
            //各頂点から左、上に行ってどこにカメラを置かなきゃいけないかを考える。
            //容量はH*Wあれば十分そう
            int x;
            for (int k=0;k<i+1;k++){
                if (S[i-k][j]=='.'){
                    x=i-k;
                }else{
                    break;
                }
            }
            int y;
            for (int k=0;k<j+1;k++){
                if (S[i][j-k]=='.'){
                    y=j-k;
                }else{
                    break;
                }
            }
            //(x,j)と(i,y)の少なくとも片方にカメラを置かなければならない
            graph.add_edge(x*W+j,H*W+i*W+y,H*W);
        }
    }
    for (int i=0;i<H;i++){
        for (int j=0;j<W;j++){
            graph.add_edge(H*W*2,i*W+j,1);
            graph.add_edge(H*W+i*W+j,H*W*2+1,1);
        }
    }
    int ans = graph.flow(H*W*2,H*W*2+1);
    cout << ans << endl;
}
