#include <iostream>
#include <vector>
#include <utility>
#include <cmath>
#include <algorithm>
#include <numeric>
#include <queue>
using namespace std;

// 点の情報を格納する構造体
struct Point {
    int id;       // グラフにおける頂点番号 (0からM+N)
    long long x, y; // 座標
    int type;     // 0: R, 1: x (加工装置), 2: y (仕分け装置)
};

// 辺の情報を格納する構造体 (Kruskal法用)
struct Edge {
    int u, v;
    long long weight;
    bool operator<(const Edge& other) const {
        return weight < other.weight;
    }
};

// Disjoint Set Union (DSU) データ構造
struct DSU {
    vector<int> parent;
    DSU(int n) {
        parent.resize(n);
        iota(parent.begin(), parent.end(), 0);
    }
    int find(int i) {
        if (parent[i] == i) return i;
        return parent[i] = find(parent[i]);
    }
    void unite(int i, int j) {
        int root_i = find(i);
        int root_j = find(j);
        if (root_i != root_j) {
            parent[root_i] = root_j;
        }
    }
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

    // --- ステップ1: 最小全域木(MST)で連結グラフを構築し、有向化 ---
    vector<Edge> all_possible_edges;
    for (int i = 0; i < total_points; ++i) {
        for (int j = i + 1; j < total_points; ++j) {
            all_possible_edges.push_back({i, j, distSq(all_points[i], all_points[j])});
        }
    }
    sort(all_possible_edges.begin(), all_possible_edges.end());

    vector<pair<int, int>> undirected_edges;
    DSU dsu(total_points);
    for (const auto& edge : all_possible_edges) {
        if (dsu.find(edge.u) != dsu.find(edge.v)) {
            dsu.unite(edge.u, edge.v);
            undirected_edges.push_back({edge.u, edge.v});
        }
    }

    vector<vector<int>> initial_adj(total_points);
    const Point& R = all_points[0];
    for (const auto& edge : undirected_edges) {
        const auto& p1 = all_points[edge.first];
        const auto& p2 = all_points[edge.second];
        long long d1 = distSq(R, p1);
        long long d2 = distSq(R, p2);

        if (d1 < d2) {
            initial_adj[p1.id].push_back(p2.id);
        } else if (d2 < d1) {
            initial_adj[p2.id].push_back(p1.id);
        } else { // 距離が同じ場合はIDで決定
            if (p1.id < p2.id) initial_adj[p1.id].push_back(p2.id);
            else initial_adj[p2.id].push_back(p1.id);
        }
    }

    // --- ステップ2: Rからの到達可能性を判定 ---
    vector<bool> is_reachable(total_points, false);
    queue<int> q;

    is_reachable[0] = true;
    q.push(0);
    while(!q.empty()){
        int u = q.front();
        q.pop();
        for(int v : initial_adj[u]){
            if(!is_reachable[v]){
                is_reachable[v] = true;
                q.push(v);
            }
        }
    }

    // --- ステップ3: 候補となる辺の選定 ---
    vector<pair<int, int>> candidate_edges;

    // R (頂点0) の処理
    if (!initial_adj[0].empty()) {
        auto& neighbors = initial_adj[0];
        auto min_it = min_element(neighbors.begin(), neighbors.end(), [&](int a, int b) {
            return distSq(all_points[0], all_points[a]) < distSq(all_points[0], all_points[b]);
        });
        candidate_edges.push_back({0, *min_it});
    }

    // x_i (加工装置) の処理
    for (int i = 1 + N; i < 1 + N + M; ++i) {
        // Rから到達可能で、かつ出次数が1以上の場合のみ処理
        if (is_reachable[i] && !initial_adj[i].empty()) {
            auto& neighbors = initial_adj[i];
            sort(neighbors.begin(), neighbors.end(), [&](int a, int b) {
                return distSq(all_points[i], all_points[a]) < distSq(all_points[i], all_points[b]);
            });
            int edges_to_add = min((int)neighbors.size(), 2);
            for (int j = 0; j < edges_to_add; ++j) {
                candidate_edges.push_back({i, neighbors[j]});
            }
        }
    }
    
    // --- ステップ4: 問題のあるxノードがなくなるまで反復的に辺を削除 ---
    while (true) {
        vector<int> in_degree(total_points, 0);
        vector<int> out_degree(total_points, 0);
        for (const auto& edge : candidate_edges) {
            out_degree[edge.first]++;
            in_degree[edge.second]++;
        }

        vector<int> problem_nodes;
        for (int i = 1 + N; i < 1 + N + M; ++i) {
            if (all_points[i].type == 1 && in_degree[i] > 0 && out_degree[i] == 0) {
                problem_nodes.push_back(i);
            }
        }

        if (problem_nodes.empty()) {
            break; // 問題がなければループを抜ける
        }

        vector<bool> is_problem_node(total_points, false);
        for (int node_id : problem_nodes) {
            is_problem_node[node_id] = true;
        }

        vector<pair<int, int>> next_candidate_edges;
        for (const auto& edge : candidate_edges) {
            if (!is_problem_node[edge.second]) {
                next_candidate_edges.push_back(edge);
            }
        }
        
        if (next_candidate_edges.size() == candidate_edges.size()) {
            break; // 変化がなければ（万が一の無限ループ防止）
        }
        candidate_edges = next_candidate_edges;
    }

    // --- 結果の出力 ---
    cout << candidate_edges.size() << endl;
    for (const auto& edge : candidate_edges) {
        cout << edge.first << " " << edge.second << endl;
    }

    
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
        cout << d[i%N] << " " <<  ans_edges[N + i].first << " " << ans_edges[N + i].second << endl;
    }

    return 0;
}