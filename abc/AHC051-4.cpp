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
// ポテンシャル関数を計算する関数
double potential(const Point& p1,vector<Point>& all_points) {
    long long pot = 1000000000;
    for (const auto& p2 : all_points) {
        pot = min(pot,distSq(p1, p2));
    }
    double mother = distSq(p1, {0,0, 5000, 0});
    return mother/(mother + pot);
}

int main() {
    // 高速化のための設定
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, K;
    cin >> N >> M >> K; // N: yの数, M: xの数, Kは未使用

    vector<Point> all_points;
    vector<Point> Processing_equipment_installation;
    int current_id = 0;

    // ルート頂点Rを(0, 5000)として追加
    all_points.push_back({current_id++, 0, 5000, 0});
    // N個の加工装置の座標を読み込み、リストに追加
    for (int i = 0; i < N; ++i) {
        long long px, py;
        cin >> px >> py;
        all_points.push_back({current_id++, px, py, 2}); // type 2: y
        Processing_equipment_installation.push_back({current_id++, px, py, 2}); // type 2: y
    }

    // M個の仕分け装置の座標を読み込み、リストに追加
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
        //float k = potential(all_points[u_idx], Processing_equipment_installation);
        //cout << k << endl;
        if (potential(all_points[u_idx], Processing_equipment_installation) < potential(all_points[v_idx],Processing_equipment_installation)) {
            initial_adj[u_idx].push_back(v_idx);
            //cout << u_idx << " " << v_idx << endl;
        } else {
            initial_adj[v_idx].push_back(u_idx);
            //cout << v_idx << " " << u_idx << endl;
        }
    }

    // --- ステップ3: 次数制約に基づき最終的なグラフを構築 ---
    vector<vector<int>> adj_after_removing(total_points);
    vector<pair<int,int>> ans_edges(N + M + 1, {-1, -1});
    //　深さ優先探索を用いて、部分グラフを選ぶ
    vector<int> out_nodes(N + M + 1, 0);
    vector<bool> visited(N + M + 1, false);
    vector<int> stack;
    stack.push_back(0);
    while (!stack.empty()) {
        int u = stack.back();
        stack.pop_back();
        if (visited[u]) continue;
        visited[u] = true;
        for (int v : initial_adj[u]) {
            // 出次数の制約を満たすなら採択
            if ((u > N && out_nodes[u] < 2) || (u == 0 && out_nodes[u] < 1)) {
                //cout << u << " " << v << endl;
                adj_after_removing[u].push_back(v);
                if (ans_edges[u].first == -1) {
                    ans_edges[u] = {v - 1, v - 1}; // 最初の辺を記録
                } else {
                    ans_edges[u].second = v - 1; // 2本目の辺を記録
                }
                stack.push_back(v);
                out_nodes[u]++;
            }
        }
    }

    // --- 結果の出力 ---

    vector<int> d(N);
    for (int i = 1; i <= N; i++) {
        d[i-1] = i;
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
