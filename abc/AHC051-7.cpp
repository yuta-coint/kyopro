//とりあえずの提出
#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>
#include <queue>

using namespace std;

// 点の構造体
// 配列のインデックスをそのままIDとして扱う
// 0: R
// 1..N: x_i (加工装置 - 終点)
// N+1..N+M: y_i (仕分け機 - 中継点)

// 点の情報を格納する構造体
struct Point {
    int id;       // グラフにおける頂点番号 (0からM+N)
    long long x, y; // 座標
    int type;     // 0: R, 1: x (加工装置), 2: y (仕分け装置)
};

// 2点間の距離の2乗を計算
double distSq(Point p1, Point p2) {
    return (p1.x - p2.x) * (p1.x - p2.x) + (p1.y - p2.y) * (p1.y - p2.y);
}

// 3点の位置関係を判定する関数
// 戻り値:
// 0 --> p, q, r は同一直線上
// 1 --> 時計回り
// 2 --> 反時計回り
int orientation(Point p, Point q, Point r) {
    double val = (q.y - p.y) * (r.x - q.x) - (q.x - p.x) * (r.y - q.y);
    if (abs(val) < 1e-10) return 0; // 同一直線上
    return (val > 0) ? 1 : 2; // 時計回り or 反時計回り
}

// 2つの線分 p1-q1 と p2-q2 が交差するか判定する関数
// (端点を共有する場合は交差とみなさない)
bool doIntersect(Point p1, Point q1, Point p2, Point q2) {
    // 2つの線分が同一、または逆向きの同一線分の場合
    if ((p1.x == p2.x && p1.y == p2.y) && (q1.x == q2.x && q1.y == q2.y)) return false;
    if ((p1.x == q2.x && p1.y == q2.y) && (q1.x == p2.x && q1.y == p2.y)) return false;

    // 端点を共有している場合は交差ではない
    if ((p1.x == p2.x && p1.y == p2.y) || (p1.x == q2.x && p1.y == q2.y) ||
        (q1.x == p2.x && q1.y == p2.y) || (q1.x == q2.x && q1.y == q2.y)) {
        return false;
    }

    // 4つの点の位置関係を調べる
    int o1 = orientation(p1, q1, p2);
    int o2 = orientation(p1, q1, q2);
    int o3 = orientation(p2, q2, p1);
    int o4 = orientation(p2, q2, q1);

    // 一般的な交差のケース
    if (o1 != o2 && o3 != o4) {
        return true;
    }

    // 同一直線上にある特殊なケースは、このアルゴリズムの単純化のため考慮しない
    return false;
}

// 結果を出力するためのヘルパー関数
//void print_edge(int u_idx, int v_idx, int N) {
//    if (u_idx == 0) {
//        cout << "R ";
//    } else { // u_idx は y ノードのはず
//        cout << "y" << u_idx - N << " ";
//    }

//    if (v_idx > N) { // v_idx が y ノードの場合
//        cout << "y" << v_idx - N << "\n";
//    } else { // v_idx が x ノードの場合
//        cout << "x" << v_idx << "\n";
//    }
//}
vector<vector<double>> calculate_arrival_probs(
    int N,
    int M,
    const vector<pair<int, int>>& ans_edges,
    const vector<int>& sorter_assignments,
    const vector<vector<double>>& p)
{
    int total_nodes = N + M + 1;
    vector<vector<double>> arrival_probs(total_nodes, vector<double>(N, 0.0));

    // --- 1. トポロジカルソートで計算順序を決定 ---
    vector<int> in_degree(total_nodes, 0);
    vector<vector<int>> adj(total_nodes); // グラフの隣接リスト表現

    for (int i = 0; i < total_nodes; ++i) {
        // ans_edgesに不正なID(範囲外)が入っていないかチェック
        if (ans_edges[i].first != -1) {
            if(ans_edges[i].first < total_nodes) { // 安全対策
                adj[i].push_back(ans_edges[i].first);
                in_degree[ans_edges[i].first]++;
            }
        }
        if (ans_edges[i].second != -1 && ans_edges[i].first != ans_edges[i].second) {
            if(ans_edges[i].second < total_nodes) { // 安全対策
                adj[i].push_back(ans_edges[i].second);
                in_degree[ans_edges[i].second]++;
            }
        }
    }

    queue<int> q;
    for (int i = 0; i < total_nodes; ++i) {
        if (in_degree[i] == 0) {
            q.push(i);
        }
    }

    vector<int> sorted_nodes;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        sorted_nodes.push_back(u);

        for (int v : adj[u]) {
            in_degree[v]--;
            if (in_degree[v] == 0) {
                q.push(v);
            }
        }
    }

    // --- 2. 確率計算 ---
    for (int j = 0; j < N; ++j) {
        arrival_probs[0][j] = 1.0;

        for (int u : sorted_nodes) {
            double current_prob = arrival_probs[u][j];
            if (current_prob == 0.0) continue;
            if (ans_edges[u].first == -1) continue;
            

            if (u > N) { // 仕分け装置の場合
                int v1 = ans_edges[u].first;
                int v2 = ans_edges[u].second;
                            
                int sorter_idx = u - N - 1; 

                // 念のため、計算したインデックスが範囲内かチェック (本来不要なはず)
                if (sorter_idx < 0 || static_cast<size_t>(sorter_idx) >= sorter_assignments.size()) continue;

                int sorter_type_k = sorter_assignments[sorter_idx];

                // sorter_type_kが-1でない（=分別器が割り当てられている）場合のみ確率pを使用
                if (sorter_type_k != -1) {
                    // 安全対策: sorter_type_k と j が p の範囲内か確認
                    if (sorter_type_k < p.size() && j < p[sorter_type_k].size()) {
                        double p_kj = p[sorter_type_k][j];
                        arrival_probs[v1][j] += current_prob * p_kj;
                        if (v2 != -1) {
                            arrival_probs[v2][j] += current_prob * (1.0 - p_kj);
                        }
                    }
                } else {
                    // 割り当てがない場合の処理（ここでは仮に0.5で均等に分配）
                    arrival_probs[v1][j] += current_prob * 0.5;
                    if (v2 != -1) {
                        arrival_probs[v2][j] += current_prob * 0.5;
                    }
                }

            } else { // ルートR または 加工装置の場合
                int v = ans_edges[u].first;
                arrival_probs[v][j] += current_prob;
            }
        }
    }
    return arrival_probs;
}
vector<int> d_assignments_tsp(vector<vector<double>>& p_matrix, int N) {
    vector<double> max_scores(1 << N, 0.0);
    vector<int> pop_count(1 << N, 0);
    vector<int> next_nodes(1 << N, -1);
    for (int i = 0; i < (1 << N); ++i) {
        int k = pop_count[i];
        for (int j = 0; j < N; ++j) {
            if ((i & (1 << j)) == 0) { // jが未訪問
                pop_count[i | (1 << j)] = k + 1;
                int next_mask = i | (1 << j);
                // 頂点jにゴミpop_count[j]がたどり着く確率を足している
                double score = max_scores[i] + p_matrix[j][k];
                if (score > max_scores[next_mask]) {
                    max_scores[next_mask] = score;
                    next_nodes[next_mask] = j;
                }
            }
        }
    }
    vector<int> d_assignments(N);
    int mask = (1 << N) - 1;
    // iはゴミ
    for (int i = N - 1; i >= 0; i--) {
        //cout << next_nodes[mask] << endl;
        d_assignments[next_nodes[mask]] = i;
        mask ^= (1 << next_nodes[mask]);
    }
    return d_assignments;
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int N, M, K;
    cin >> N >> M >> K; // Kの用途は不明

    int total_nodes = 1 + N + M;
    vector<Point> points(total_nodes);
    vector<Point> sorters(M);
    
    // R (始点) は (0, 0) と仮定
    points[0] = {0, 0, 5000, 0}; 

    // x (加工装置) の座標を読み込み (ID: 1..N) - 終点
    for (int i = 1; i <= N; i++) {
        cin >> points[i].x >> points[i].y;
        points[i].id = i;
        points[i].type = 1; // 加工装置
    }

    // y (仕分け機) の座標を読み込み (ID: N+1..N+M) - 中継点
    for (int i = 1; i <= M; i++) {
        cin >> points[N + i].x >> points[N + i].y;
        points[N + i].id = N + i;
        points[N + i].type = 2; // 仕分け機
        sorters[i - 1] = points[N + i]; // 仕分け機の情報を保存
    }

    vector<int> in_degree(total_nodes, 0);
    vector<int> out_degree(total_nodes, 0);
    vector<pair<int, int>> edges;

    // --- アルゴリズム本体 ---

    // 1. Rから最も近い y (仕分け機) を見つける
    if (M > 0) {
        int first_y_idx = -1;
        double min_dist_sq = -1.0;

        for (int i = 1; i <= M; ++i) {
            int y_node_idx = N + i;
            double d = distSq(points[0], points[y_node_idx]);
            if (first_y_idx == -1 || d < min_dist_sq) {
                min_dist_sq = d;
                first_y_idx = y_node_idx;
            }
        }
        
        if (first_y_idx != -1) {
            edges.push_back({0, first_y_idx});
            out_degree[0]++;
            in_degree[first_y_idx]++;
        }
    }

    // 2. 木構造を構築していく (BFSベースで y から y または x へ)
    queue<int> q;
    for(int i = 1; i <= M; ++i) {
        int y_node_idx = N + i;
        if (in_degree[y_node_idx] > 0) {
            q.push(y_node_idx);
        }
    }

    while(!q.empty()){
        int u_idx = q.front(); // u_idx は y ノード
        q.pop();

        // 接続候補を集める (まだどの木にも属していない y と x)
        vector<pair<double, int>> candidates;
        // 他の y ノード
        for (int i = 1; i <= M; ++i) {
            int y_node_idx = N + i;
            if (in_degree[y_node_idx] == 0) { // まだ木に属していないy
                candidates.push_back({distSq(points[u_idx], points[y_node_idx]), y_node_idx});
            }
        }
        // x ノード
        for (int i = 1; i <= N; ++i) {
            if (in_degree[i] == 0) { // まだ接続されていないx
                 candidates.push_back({distSq(points[u_idx], points[i]), i});
            }
        }

        sort(candidates.begin(), candidates.end()); // 距離が近い順にソート

        for (auto const& [dist, v_idx] : candidates) {
            if (out_degree[u_idx] >= 2) break; // yの出次数は2以下
            if (in_degree[v_idx] > 0) continue; // 接続先は木に属していてはならない(閉路回避)

            // 交差チェック
            bool intersects = false;
            for (const auto& edge : edges) {
                if (doIntersect(points[u_idx], points[v_idx], points[edge.first], points[edge.second])) {
                    intersects = true;
                    break;
                }
            }

            if (!intersects) {
                edges.push_back({u_idx, v_idx});
                out_degree[u_idx]++;
                in_degree[v_idx]++;
                
                if (v_idx > N) { // vがyならキューに追加して探索を続ける
                    q.push(v_idx);
                }
            }
        }
    }
    
    // 3. 未接続のx(加工装置)が残っている場合、最も近い接続可能なyに接続する
    for (int i = 1; i <= N; ++i) {
        int x_idx = i;
        if (in_degree[x_idx] == 0) {
            vector<pair<double, int>> y_candidates;
            for (int j = 1; j <= M; ++j) {
                int y_idx = N + j;
                if (out_degree[y_idx] < 2) { // 出次数に余裕のあるy
                    y_candidates.push_back({distSq(points[x_idx], points[y_idx]), y_idx});
                }
            }
            sort(y_candidates.begin(), y_candidates.end());

            for (auto const& [dist, y_idx] : y_candidates) {
                bool intersects = false;
                for (const auto& edge : edges) {
                    if (doIntersect(points[y_idx], points[x_idx], points[edge.first], points[edge.second])) {
                        intersects = true;
                        break;
                    }
                }
                if (!intersects) {
                    edges.push_back({y_idx, x_idx});
                    out_degree[y_idx]++;
                    in_degree[x_idx]++;
                    break; // 接続できたら次のxへ
                }
            }
        }
    }
    
    // 4. 出次数が0のyノードを削除
    //　仕上げ処理（出次数がゼロの頂点を全て潰す作業）
    vector<pair<int, int>> ans_edges(N + M + 1, {-1, -1});
    for (const auto& edge : edges) {
        int u_idx = edge.first;
        int v_idx = edge.second;
        if (ans_edges[u_idx].first == -1) {
            ans_edges[u_idx] = {v_idx, v_idx}; // 最初の辺を記録
        } else {
            ans_edges[u_idx].second = v_idx; // 2本目の辺を記録
        }
    }
    vector<vector<int>> reverse_edges(N + M + 1);
    vector<bool> is_used(N + M + 1, false);
    for (int i = 0; i < N + M + 1; i++) {
        if (ans_edges[i].first != -1) {
            reverse_edges[ans_edges[i].first].push_back(i);
            is_used[ans_edges[i].first] = true;
            if (ans_edges[i].second == -1) {
                continue;
            }
            if (ans_edges[i].second != ans_edges[i].first) {
                reverse_edges[ans_edges[i].second].push_back(i);
            }
            is_used[ans_edges[i].second] = true;
        }
    }
    vector<int> zero_out_degree;
    for (int i = N + 1; i < N + M + 1; i++) {
        if (is_used[i]){
            if (ans_edges[i].first == -1) {
                zero_out_degree.push_back(i);
            }
        }
    }
    // 出次数がゼロの頂点を削除
    while (!zero_out_degree.empty()) {
        int current = zero_out_degree.back();
        zero_out_degree.pop_back();
        if (current <= N){
          continue;
        }
        is_used[current] = false; // 削除済みとしてマーク
        for (const int &j : reverse_edges[current]) {
            if (ans_edges[j].first == current && ans_edges[j].second == current) {
                ans_edges[j] = {-1, -1}; // エッジを削除
                zero_out_degree.push_back(j);
            }else if (ans_edges[j].first == current) {
                if (ans_edges[j].second == -1) {
                    ans_edges[j] = {-1, -1}; // エッジの頂点番号を調整
                    zero_out_degree.push_back(j);
                } else{
                    ans_edges[j] = {ans_edges[j].second, ans_edges[j].second}; // エッジの頂点番号を調整
                }
            } else if (ans_edges[j].second == current) {
                ans_edges[j].second = ans_edges[j].first; // エッジの頂点番号を調整
            }
        }
    }

    
    vector<vector<double>> p(K);
    for (int i = 0; i < K; i++){
        for (int j = 0; j < N; j ++){
            double tmp;
            cin >> tmp;
            p[i].push_back(tmp); // 入力を0-indexedに変換
        }
    }

    // 1. 分別器の割り当て
    //   - 各分別器kのスコアを計算し、ペア(スコア, k)のvectorを作る
    vector<pair<double, int>> sorter_scores;
    for (int k = 0; k < K; ++k) {
        double score = 0.0;
        for (int j = 0; j < N; ++j) {
            score += abs(p[k][j] - 0.5);
        }
        sorter_scores.push_back({score, k});
    }

    //   - スコアで降順ソート
    sort(sorter_scores.rbegin(), sorter_scores.rend());

    //   - 使用する分別器設置場所に、スコアの高い順から割り当て
    sort(sorters.begin(), sorters.end(), [](const Point& a, const Point& b) {
        return a.x < b.x;
    });
    vector<int> sorter_assignments(M, -1);
    for (int i = 0; i < M; ++i) {
        // FIXED: Added static_cast to prevent signed/unsigned comparison warning
        if (static_cast<size_t>(i) < sorter_scores.size()) {
            sorter_assignments[sorters[i].id - N - 1] = sorter_scores[i].second; // スコアの高い順に割り当て
        } else {
            sorter_assignments[sorters[i].id - N - 1] = i % K; // 割り当てられない場合はテキトーに
        }
    }

    // 2. 処理装置の割り当て
    vector<vector<double>> W = calculate_arrival_probs(N, M, ans_edges, sorter_assignments, p);

    //　結果の出力
    vector<vector<double>> sub_W;
    for (int i = 1; i <= N; ++i) {
        sub_W.push_back(W[i]);
    }
    vector<int> d = d_assignments_tsp(sub_W, N);

    //for (int i = 0; i < N-1; i++){
    //    cout << sub_W[i][0] << " ";
    //}
    //cout << sub_W[N-1][0] << endl;
    
    for (int i = 0; i < N-1; i++){
        cout << d[i] << " ";
    }
    cout << d[N-1] << endl;
    cout << ans_edges[0].first - 1 << endl;
    for (int i = 1; i <= M; i++) {
        if (ans_edges[i + N].first == -1) {
            cout << -1 << endl; // 出次数が0の場合は-1と出力
            continue;
        }
        cout << d[i%N] << " " <<  ans_edges[N + i].first - 1 << " " << ans_edges[N + i].second -1 << endl;
    }

    return 0;
}