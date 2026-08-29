#include <iostream>
#include <vector>
#include <utility>
#include <cmath>
#include <algorithm>
#include <queue>
using namespace std;
// 点の情報を格納する構造体
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
            
            // 安全対策: uがsorter_assignmentsの範囲内か確認
            if (u >= sorter_assignments.size()) continue;

            if (u > N) { // 仕分け装置の場合
                int v1 = ans_edges[u].first;
                int v2 = ans_edges[u].second;
                
                int sorter_type_k = sorter_assignments[u];

                // ★★★ ここからが修正箇所 ★★★
                // sorter_type_kが-1でない（=分別器が割り当てられている）場合のみ確率pを使用
                if (sorter_type_k != -1) {
                    // 安全対策: sorter_type_k と j が p の範囲内か確認
                    if (sorter_type_k < p.size() && j < p[sorter_type_k].size()) {
                        double p_kj = p[sorter_type_k][j];
                        arrival_probs[v1][j] += current_prob * p_kj;
                        if (v1 != v2 && v2 != -1) {
                            arrival_probs[v2][j] += current_prob * (1.0 - p_kj);
                        }
                    }
                } else {
                    // 割り当てがない場合の処理（ここでは仮に0.5で均等に分配）
                    arrival_probs[v1][j] += current_prob * 0.5;
                    if (v1 != v2 && v2 != -1) {
                        arrival_probs[v2][j] += current_prob * 0.5;
                    }
                }
                // ★★★ 修正箇所ここまで ★★★

            } else { // ルートR または 加工装置の場合
                int v = ans_edges[u].first;
                arrival_probs[v][j] += current_prob;
            }
        }
    }
    return arrival_probs;
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
            // FIXED: Added static_cast to prevent signed/unsigned comparison warning
            while (current_x >= point_classes[k][counter[k]].x){
                counter[k]++;
                if (static_cast<size_t>(counter[k]) >= point_classes[k].size()) {
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
                if (W[i+1][j] > max_prob) {
                    max_prob = W[i+1][j];
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


    for (int i = 0; i < N-1; i++){
        cout << d_assignments[i] << " ";
    }
    cout << d_assignments[N-1] << endl;
    
    cout << ans_edges[0].first - 1 << endl;
    for (int i = 1; i <= M; i++) {
        if (ans_edges[i + N].first == -1) {
            cout << -1 << endl; // 出次数が0の場合は-1と出力
            continue;
        }
        cout << sorter_assignments[i-1] << " " <<  ans_edges[N + i].first - 1 << " " << ans_edges[N + i].second -1 << endl;
    }
    return 0;
}