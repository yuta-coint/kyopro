#include <iostream>
#include <vector>
#include <utility>
#include <cmath>
#include <algorithm>
using namespace std;

// 点の情報を格納する構造体
struct Point {
    int id;       // グラフにおける頂点番号 (0からM+N)
    long long x, y; // 座標
    int type;     // 0: R, 1: x (加工装置), 2: y (仕分け装置)
};

// 2点間の距離の2乗を計算する関数
long long distSq(const Point& p1, const Point& p2) {
    return (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y);
}

int main() {
    // 高速化のための設定
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, K;
    cin >> N >> M >> K; // N: yの数, M: xの数, Kは未使用

    vector<Point> all_points;
    int current_id = 0;

    // ルート頂点Rを(0, 5000)として追加
    all_points.push_back({current_id++, 0, 5000, 0});

    // N個の仕分け装置(y_j)の座標を読み込み、リストに追加
    for (int i = 0; i < N; ++i) {
        long long px, py;
        cin >> px >> py;
        all_points.push_back({current_id++, px, py, 2}); // type 2: y
    }

    // M個の加工装置(x_i)の座標を読み込み、リストに追加
    for (int i = 0; i < M; ++i) {
        long long px, py;
        cin >> px >> py;
        all_points.push_back({current_id++, px, py, 1}); // type 1: x
    }

    int total_points = all_points.size();

    // --- ステップ1: ガブリエルグラフの構築 (平面グラフ) ---
    vector<pair<int, int>> undirected_edges;
    for (int i = 0; i < total_points; ++i) {
        for (int j = i + 1; j < total_points; ++j) {
            const auto& p1 = all_points[i];
            const auto& p2 = all_points[j];

            long double mid_x = (long double)(p1.x + p2.x) / 2.0;
            long double mid_y = (long double)(p1.y + p2.y) / 2.0;
            long double radius_sq = ((long double)p1.x - mid_x) * ((long double)p1.x - mid_x) +
                                  ((long double)p1.y - mid_y) * ((long double)p1.y - mid_y);

            bool is_gabriel_edge = true;
            for (int k = 0; k < total_points; ++k) {
                if (k == i || k == j) continue;
                const auto& pk = all_points[k];
                long double d_sq = ((long double)pk.x - mid_x) * ((long double)pk.x - mid_x) +
                                   ((long double)pk.y - mid_y) * ((long double)pk.y - mid_y);
                if (d_sq < radius_sq) {
                    is_gabriel_edge = false;
                    break;
                }
            }

            if (is_gabriel_edge) {
                undirected_edges.push_back({i, j});
            }
        }
    }

    // --- ステップ2: 有向化 (DAGの作成) ---
    vector<vector<int>> initial_adj(total_points);
    const Point& R = all_points[0];
    for (const auto& edge : undirected_edges) {
        int u_idx = edge.first;
        int v_idx = edge.second;
        // Rからの距離(ポテンシャル)が小さい方から大きい方へ辺を向ける
        if (distSq(R, all_points[u_idx]) < distSq(R, all_points[v_idx])) {
            initial_adj[u_idx].push_back(v_idx);
        } else {
            initial_adj[v_idx].push_back(u_idx);
        }
    }

    // --- ステップ3: 次数制約に基づき最終的なグラフを構築 ---
    vector<pair<int, int>> final_edges;

    vector<pair<int,int>> ans_edges(N + M + 1, {-1, -1});

    // R (頂点0) の処理: 出次数を1にする
    if (!initial_adj[0].empty()) {
        auto& neighbors = initial_adj[0];
        // Rに最も近い頂点への辺を1本だけ選ぶ
        auto min_it = min_element(neighbors.begin(), neighbors.end(), [&](int a, int b) {
            return distSq(all_points[0], all_points[a]) < distSq(all_points[0], all_points[b]);
        });
        final_edges.push_back({0, *min_it});
        ans_edges[0] = {*min_it - 1, -1};
    }

    // x_i (加工装置) の処理: 出次数を1か2にする
    // x_iのIDは 1+N から 1+N+M-1 まで
    for (int i = 1 + N; i < 1 + N + M; ++i) {
        if (initial_adj[i].empty()) continue;
        
        auto& neighbors = initial_adj[i];
        // x_iからの距離が近い順にソート
        sort(neighbors.begin(), neighbors.end(), [&](int a, int b) {
            return distSq(all_points[i], all_points[a]) < distSq(all_points[i], all_points[b]);
        });
        
        // 最大2本まで辺を追加
        int edges_to_add = min((int)neighbors.size(), 2);
        for (int j = 0; j < edges_to_add; ++j) {
            final_edges.push_back({i, neighbors[j]});
            if (j == 0){
                ans_edges[i] = {neighbors[j] - 1, neighbors[j] - 1};
            } else {
                ans_edges[i].second = neighbors[j] - 1;
            };
        }
    }
    
    // y_j (仕分け装置) の処理: 出次数は0なので、何もしない

    // 注意: このアルゴリズムでは、y_jの入次数が1以上になることは保証されません。
    // 孤立したy_jが生成される可能性はありますが、他のすべての条件は満たします。

    // --- 結果の出力 ---
    
    vector<int> d(N);
    for (int i = 1; i <= N; i++) {
        d[i] = i;
    }

    for (int i = 0; i < N-1; i++){
        cout << d[i] << " ";
    }
    cout << d[N-1] << endl;
    cout << ans_edges[0].first << endl;
    for (int i = 1; i <= M; i++) {
        if (ans_edges[i + N].first == -1) {
            cout << -1 << endl; // 出次数が0の場合は-1と出力
            continue;
        }
        cout << d[i%13] << " " <<  ans_edges[N + i].first << " " << ans_edges[N + i].second << endl;
    }
    return 0;
}
