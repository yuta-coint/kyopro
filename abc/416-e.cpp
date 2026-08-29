#include <bits/stdc++.h>
#include <atcoder/all>
using namespace std;
using namespace atcoder;
typedef long long ll;
int main(){
    int N, M;
    cin >> N >> M;
    ll ans = 0;
    vector<vector<ll>> dist(N+1, vector<ll>(N+1, -1));
    for (int i = 0; i <= N; i++){
        dist[i][i] = 0;
    }
    for (int i = 0; i < M; i++){
        int a, b;
        ll c;
        cin >> a >> b >> c;
        if (dist[a][b] == -1 || dist[a][b] > 2*c){
            dist[a][b] = 2*c;
            dist[b][a] = 2*c;
        }
    }
    int K;
    ll T;
    cin >> K >> T;
    for (int i = 0; i < K; i++){
        int d;
        cin >> d;
        dist[0][d] = T;
        dist[d][0] = T;
    }

    for (int k = 0; k <= N; k++){
        for (int i = 0; i <= N; i++){
            for (int j = 0; j <= N; j++){
                if (dist[i][k] != -1 && dist[k][j] != -1){
                    if (dist[i][j] == -1 || dist[i][j] > dist[i][k] + dist[k][j]){
                        dist[i][j] = dist[i][k] + dist[k][j];
                    }
                }
            }
        }
    }

    int Q;
    cin >> Q;
    while (Q--){
        int type;
        cin >> type;
        if (type == 1 || type == 2){
            int x, y;
            ll t;
            if (type == 1){
                cin >> x >> y >> t;
                t *=2;
            }else{
                cin >> x;
                y = 0;
                t = T;
            }
            vector<vector<ll>> new_dist = dist;
            for (int i = 0; i <= N; i++){
                for (int j = 0; j <= N; j++){
                    if (dist[i][x] != -1 && dist[y][j] != -1){
                        if (dist[i][j] == -1 || dist[i][j] > dist[i][x] + t + dist[y][j]){
                            new_dist[i][j] = new_dist[i][x] + t + new_dist[y][j];
                        }
                    }
                    if (dist[i][y] != -1 && dist[x][j] != -1){
                        if (dist[i][j] == -1 || dist[i][j] > dist[i][y] + t + dist[x][j]){
                            new_dist[i][j] = new_dist[i][y] + t + new_dist[x][j];
                        }
                    }
                }
            }
            dist = new_dist;
        }else if (type == 3){
            ans = 0;
            for (int i = 1; i <= N; i++){
                for (int j = i + 1; j <= N; j++){
                    if (dist[i][j] != -1){
                        ans += dist[i][j];
                    }
                }
            }
            cout << ans << endl;
        }
    }
    return 0;
}