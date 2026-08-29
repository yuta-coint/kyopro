#include <iostream>
#include <vector>
#include <utility>
#include <cmath>
#include <algorithm>
using namespace std;
// 点の情報を格納する構造体
ll calculate_score(
    int N, int M, int K,
    const vector<vector<double>>& p_matrix,
    const vector<int>& d_assignments,
    int inlet_dest,
    const vector<pair<int, int>>& sorter_configs
) {
    int num_nodes = N + M;

    // 各ノードに各種類のゴミが到達する確率
    // probs[node_id][waste_type]
    vector<vector<double>> probs(num_nodes, std::vector<double>(N, 0.0));

    // 搬入口から流れ込む初期確率を設定
    if (inlet_dest >= 0 && inlet_dest < num_nodes) {
        for (int i = 0; i < N; ++i) {
            probs[inlet_dest][i] = 1.0;
        }
    }

    // トポロジカルソート順（≒BFS順）で確率を伝播させる
    // グラフがDAGであることが保証されているため、単純なBFSで上流から処理できる
    std::queue<int> q;
    std::vector<bool> visited(num_nodes, false);
    std::vector<int> topo_order;

    if (inlet_dest >= 0 && inlet_dest < num_nodes) {
        q.push(inlet_dest);
        visited[inlet_dest] = true;
    }

    while (!q.empty()) {
        int u = q.front();
        q.pop();
        topo_order.push_back(u);

        // uが分別器の場合、その出口に接続されているノードをキューに追加
        if (u >= N) {
            int sorter_idx = u - N;
            const auto& config = sorter_configs[sorter_idx];
            if (std::get<0>(config) != -1) {
                int v1 = std::get<1>(config);
                int v2 = std::get<2>(config);

                if (v1 >= 0 && v1 < num_nodes && !visited[v1]) {
                    visited[v1] = true;
                    q.push(v1);
                }
                if (v2 >= 0 && v2 < num_nodes && !visited[v2]) {
                    visited[v2] = true;
                    q.push(v2);
                }
            }
        }
    }
    
    // トポロジカル順にノードを処理して確率を計算
    for (int u : topo_order) {
        // uが処理装置なら、そこから先はないのでスキップ
        if (u < N) {
            continue;
        }

        // uが分別器の場合、確率を分岐させる
        int sorter_idx = u - N;
        const auto& config = sorter_configs[sorter_idx];

        // 行き先が未設置の分別器の場合、スキップ（制約違反）
        if (std::get<0>(config) == -1) {
            continue;
        }

        int k = std::get<0>(config);
        int v1 = std::get<1>(config);
        int v2 = std::get<2>(config);
        
        // 各ゴミ種について確率を計算し、次のノードに渡す
        for (int waste_type = 0; waste_type < N; ++waste_type) {
            double p_in = probs[u][waste_type];
            double p_outlet1 = p_matrix[k][waste_type];
            
            if (v1 >= 0 && v1 < num_nodes) {
                probs[v1][waste_type] += p_in * p_outlet1;
            }
            if (v2 >= 0 && v2 < num_nodes) {
                probs[v2][waste_type] += p_in * (1.0 - p_outlet1);
            }
        }
    }

    // --- 最終スコアの計算 ---

    // ゴミの種類 -> 対応する処理装置の場所ID のマッピング
    std::vector<int> waste_to_plant_map(N);
    for (int loc = 0; loc < N; ++loc) {
        waste_to_plant_map[d_assignments[loc]] = loc;
    }

    double total_q = 0.0;
    for (int i = 0; i < N; ++i) { // 各ゴミ種 i について
        // ゴミiが処理されるべき場所のID
        int target_plant_id = waste_to_plant_map[i];
        
        // ゴミiが正しい処理装置にたどり着く確率 q_i
        double q_i = probs[target_plant_id][i];
        total_q += q_i;
    }

    // スコア計算式
    double avg_q = (N > 0) ? total_q / N : 0.0;
    ll score = round(1e9 * (1.0 - avg_q));
    
    return score;
}
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
    vector<Point> Processing_equipment_installation;
    vector<vector<Point>> point_classes(8);
    int current_id = 0;

    // ルート頂点Rを(0, 5000)として追加
    all_points.push_back({current_id++, 0, 5000, 0});
    // N個の加工装置の座標を読み込み、リストに追加
    for (int i = 0; i < N; ++i) {
        long long px, py;
        cin >> px >> py;
        Processing_equipment_installation.push_back({current_id, px, py, 2}); // type 2: y
        all_points.push_back({current_id++, px, py, 2}); // type 2: y
    }

    vector<Point> sorters;
    // M個の仕分け装置の座標を読み込み、リストに追加
    for (int i = 0; i < M; ++i) {
        long long px, py;
        cin >> px >> py;
        point_classes[py/1251].push_back({current_id, px, py, 1});
        sorters.push_back({current_id, px, py, 1}); // type 1: x
        all_points.push_back({current_id++, px, py, 1}); // type 1: x
    }
    //　ソート
    for (int j = 0; j < 8; ++j) {
        sort(point_classes[j].begin(), point_classes[j].end(), [](const Point& a, const Point& b) {
            // まずx座標を比較する
            if (a.x != b.x) {
                return a.x < b.x;
            }
        // x座標が同じ場合はy座標を比較する
        return a.y < b.y;
        });
    }
    //　左すぎるごみ処理場は諦めよう。
    vector<int> counter(8, 0);
    //一番左の点をRとつなぐ。
    //vector<vector<int>> initial_adj(total_points);
    vector<pair<int,int>> ans_edges(N + M + 1, {-1, -1});
    //int min_id = -1;
    //int min_x = 1000000000;
    //int tmp = 0;
    int current_x = 0;
    int seg_counter = 1;
    vector<int> id_search(16, 0);
    for (int depth = 3; depth >= 0; depth --){
        int p_depth = 1 << depth;
        int next_x = current_x;
        for (int k = 0; k < 8; k+=p_depth){
            while (current_x >= point_classes[k][counter[k]].x){
                counter[k]++;
                if (counter[k] >= point_classes[k].size()) {
                    counter[k] -=1;
                    break;
                }
            }
            if (next_x < point_classes[k][counter[k]].x){
                next_x = point_classes[k][counter[k]].x;
            }
            int id = point_classes[k][counter[k]].id;
            int mother_id = id_search[seg_counter/2];
            if (ans_edges[mother_id].first == -1){
                ans_edges[mother_id] = {id, id};
            } else {
                ans_edges[mother_id].second = id;
            }
            id_search[seg_counter] = id;
            seg_counter++;
        }
        current_x = next_x;
    }
    //int max_x = 0;
    //int max_id = -1;
    vector<Point> tmp_points;
    vector<vector<Point>> installation_points(8);
    vector<int> max_installation(8, -1);
    //　各パートで一番x座標が大きい処理装置を見つけ出す
    for (int i = 0; i < N; i++){
        int part = Processing_equipment_installation[i].y / 1251;
        installation_points[part].push_back(Processing_equipment_installation[i]);
        if (Processing_equipment_installation[i].x > max_installation[part]) {
            max_installation[part] = Processing_equipment_installation[i].x;
        }
    }
    for (int j = 0; j < 8; j++) {
        for (const auto& point : point_classes[j]) {
            if (point.x < max_installation[j]) {
                installation_points[j].push_back(point);
            }
        }
        sort(installation_points[j].begin(), installation_points[j].end(), [](const Point& a, const Point& b) {
            return a.x < b.x;
        });
    }
    vector<int> size_of_point_classes(8, 0);
    for (int k = 0; k < 8; k++) {
        size_of_point_classes[k] = installation_points[k].size();
    }
    // あまりにも左すぎるごみ処理場は諦める。
    for (int k = 0; k < 8; k++) {
        //int class_cnt = 0;
        //int last_class = -1;
        for (int i = 1; i < size_of_point_classes[k]; i++){
            //一個前とつなげる余地があるかを調べる。
            if (point_classes[k][counter[k]].x >= installation_points[k][i].x) {
                continue; // 現在の点が前の点よりも左にある場合はスキップ
            }
            //cout << point_classes[k][counter[k]].x << " " << installation_points[k][i].x << endl;
            if (installation_points[k][i-1].id >= N){
                if (ans_edges[installation_points[k][i-1].id].first == -1){
                    ans_edges[installation_points[k][i-1].id] = {installation_points[k][i].id, installation_points[k][i].id};
                } else if ( (ans_edges[installation_points[k][i-1].id].first == ans_edges[installation_points[k][i-1].id].second) && (ans_edges[installation_points[k][i-1].id].first != -1)) {
                    ans_edges[installation_points[k][i-1].id].second = installation_points[k][i].id;
                }
            }else if (i >= 2){
                if (ans_edges[installation_points[k][i-2].id].first == -1){
                    ans_edges[installation_points[k][i-2].id] = {installation_points[k][i].id, installation_points[k][i].id};
                } else if ( (ans_edges[installation_points[k][i-2].id].first == ans_edges[installation_points[k][i-2].id].second) && (ans_edges[installation_points[k][i-2].id].first != -1)) {
                    ans_edges[installation_points[k][i-2].id].second = installation_points[k][i].id;
                }
            }
        }
    }
    //　仕上げ処理（出次数がゼロの頂点を全て潰す作業）
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
    //グラフの簡略化
    vector<pair<int, int>> simplified_edges(N + M + 1);
    vector<bool> is_used_edges(N + M + 1, false);
    for (int i = 0; i < N + M + 1; i++) {
        if (is_used_edges[i]) {
            is_used_edges[i] = true; // エッジを使用済みとしてマーク
            continue; // 既に使用済みのエッジはスキップ
        }
        if (ans_edges[i].first == -1) {
            simplified_edges[i] = {-1, -1}; // エッジが存在しない場合
            is_used_edges[i] = true; // エッジを使用済みとしてマーク
            continue;
        }
        if (ans_edges[i].second == -1){
            int j = ans_edges[i].first;
            while (j > N && ans_edges[j].second == -1) {
                is_used_edges[j] = true; // エッジを使用済みとしてマーク
                j = ans_edges[j].first; // エッジの頂点番号を調整
            }
            simplified_edges[i] = {ans_edges[j].first, -1}; // エッジの頂点番号を調整
            is_used_edges[i] = true; // エッジを使用済みとしてマーク
        }else{
            simplified_edges[i] = {ans_edges[i].first, ans_edges[i].second}; // エッジの頂点番号を調整
            is_used_edges[i] = true; // エッジを使用済みとしてマーク
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
    //    - 各分別器kのスコアを計算し、ペア(スコア, k)のvectorを作る
    vector<pair<double, int>> sorter_scores;
    for (int k = 0; k < K; ++k) {
        double score = 0.0;
        for (int j = 0; j < N; ++j) {
            score += abs(p[k][j] - 0.5);
        }
        sorter_scores.push_back({score, k});
    }

    //    - スコアで降順ソート
    sort(sorter_scores.rbegin(), sorter_scores.rend());

    //    - 使用する分別器設置場所に、スコアの高い順から割り当て
    sort(sorters.begin(), sorters.end(), [](const Point& a, const Point& b) {
        return a.x < b.x;
    });
    vector<int> sorter_assignments(M, -1);
    for (int i = 0; i < M; ++i) {
        if (i < sorter_scores.size()) {
            sorter_assignments[sorters[i].id - N - 1] = sorter_scores[i].second; // スコアの高い順に割り当て
        } else {
            sorter_assignments[sorters[i].id - N - 1] = i % M; // 割り当てられない場合は-1
        }
    }

    // 2. 処理装置の割り当て
    //    - 上記の割り当てを使って、各処理装置の場所iに各ゴミjが届く確率 W[i][j] を計算
    //      (スコア計算ロジックを流用)
    std::vector<std::vector<double>> W = calculate_arrival_probs(...);

    //    - 貪欲マッチング
    std::vector<int> d_assignments(N);
    std::vector<bool> plant_assigned(N, false);
    std::vector<bool> waste_assigned(N, false);

    for (int k = 0; k < N; ++k) {
        double max_prob = -1.0;
        int best_plant_loc = -1;
        int best_waste_type = -1;

        // 未割り当ての中から最も確率の高いペアを探す
        for (int i = 0; i < N; ++i) {
            if (plant_assigned[i]) continue;
            for (int j = 0; j < N; ++j) {
                if (waste_assigned[j]) continue;
                if (W[i][j] > max_prob) {
                    max_prob = W[i][j];
                    best_plant_loc = i;
                    best_waste_type = j;
                }
            }
        }

        // ペアを確定
        d_assignments[best_plant_loc] = best_waste_type;
        plant_assigned[best_plant_loc] = true;
        waste_assigned[best_waste_type] = true;
    }

    // これで d_assignments が完成！
    // --- 結果の出力 ---

    vector<int> d(N);
    for (int i = 0; i < N; i++) {
        d[i] = i;
    }

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
        cout << sorters[i].id - N - 1 << " " <<  ans_edges[N + i].first - 1 << " " << ans_edges[N + i].second -1 << endl;
    }
    return 0;
}