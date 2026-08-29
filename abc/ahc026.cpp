#include <bits/stdc++.h>
using namespace std;
#define ll long long

int n, m;
vector<vector<int>> initial_cond;

vector<vector<int>> cond;
int cnt_val;
vector<pair<int, int>> ans;
int cost;
vector<int> capa;
vector<int> bottom_ok;
int bottom_cnt;

int best_score = 2e9;
vector<pair<int, int>> best_ans;

mt19937 mt(42);
vector<int> current_perm;

void carry_out() {
    for (int i = 0; i < m; ++i) {
        if (capa[i] > 0) {
            if (!cond[i].empty() && cond[i].back() == cnt_val) {
                ans.push_back({cnt_val, 0});
                cnt_val++;
                cond[i].pop_back();
                capa[i]--;
                carry_out();
                return;
            }
        }
    }
}

void bottom_carry_out() {
    for (int i = 0; i < m; ++i) {
        if (capa[i] - bottom_ok[i] > 0) {
            if (cond[i].size() > bottom_ok[i] + 1 && cond[i][bottom_ok[i] + 1] == bottom_cnt) {
                bottom_cnt--;
                bottom_ok[i]++;
                bottom_carry_out();
                return;
            }
        }
    }
}

int min_max() {
    vector<int> minL(m, -1);
    for (int i = 0; i < m; ++i) {
        if (capa[i] > bottom_ok[i]) {
            int cur_min = 2e9;
            for (int val : cond[i]) cur_min = min(cur_min, val);
            minL[i] = cur_min;
        }
    }
    int max_val = -2;
    int idx = 0;
    for (int i = 0; i < m; ++i) {
        if (minL[i] > max_val) {
            max_val = minL[i];
            idx = i;
        }
    }
    return idx;
}

void move_box(int v, int target_idx) {
    for (int j = 0; j < m; ++j) {
        auto it = find(cond[j].begin(), cond[j].end(), v);
        if (it != cond[j].end()) {
            if (target_idx == j) break;
            ans.push_back({v, target_idx + 1});
            int cut_idx = distance(cond[j].begin(), it);
            int moved_cnt = cond[j].size() - cut_idx;
            cost += moved_cnt + 1;
            capa[target_idx] += moved_cnt;
            capa[j] -= moved_cnt;
            cond[target_idx].insert(cond[target_idx].end(), cond[j].begin() + cut_idx, cond[j].end());
            cond[j].erase(cond[j].begin() + cut_idx, cond[j].end());
            break;
        }
    }
}

void apply_preprocess() {
    vector<int> protected_size(m, 1);

    for (int k = 0; k < m; ++k) {
        int curr = current_perm[k];
        // (a) k=0 のとき隣へ、そうでないときは current_perm[k-1] へ丸ごと移動
        int target = (k == 0) ? (curr + 1) % m : current_perm[k - 1];
        
        // carry_out等で箱が即時回収されサイズが減った場合の調整
        for (int i = 0; i < m; ++i) {
            protected_size[i] = min(protected_size[i], (int)cond[i].size());
        }

        int p_curr = protected_size[curr];
        
        // --- 今回の追加ロジック: 他の列のトップの最大値（次に積まれる箱）を取得 ---
        int max_top = -1;
        for (int j = 0; j < m; ++j) {
            if (j == curr) continue;
            if ((int)cond[j].size() <= protected_size[j]) continue;
            max_top = max(max_top, cond[j].back());
        }
        
        // ダミーの上に箱があり、かつそれが次に積まれる箱より大きい場合、1つ残す
        if (p_curr == 1 && (int)cond[curr].size() > 1) {
            int bottom_box = cond[curr][1];
            if (max_top != -1 && bottom_box > max_top) {
                p_curr = 2; // 退避の起点を1つ上にずらし、底の箱を保護する
            }
        }
        // -------------------------------------------------------------------------

        if ((int)cond[curr].size() > p_curr) {
            // 保護されている部分（p_curr番目）より上の箱だけを移動
            move_box(cond[curr][p_curr], target);
            carry_out();
        }

        // (b) curr列目以外の列の一番上にある箱から条件を満たすものを移動
        while (true) {
            // 毎ループ調整（移動後にcarry_outが呼ばれるため）
            for (int i = 0; i < m; ++i) {
                protected_size[i] = min(protected_size[i], (int)cond[i].size());
            }

            int best_j = -1;
            int max_val = -1;
            int curr_top = cond[curr].back();

            for (int j = 0; j < m; ++j) {
                if (j == curr) continue;
                if ((int)cond[j].size() <= protected_size[j]) continue; // 保護部分のみの列はスキップ
                
                int top_val = cond[j].back();
                if (top_val < curr_top && top_val > max_val) {
                    max_val = top_val;
                    best_j = j;
                }
            }

            if (best_j != -1) {
                int target_v = max_val;
                int p_best = protected_size[best_j];
                
                // 保護されている部分（p_best）の手前までしか掘り下げない
                for (int i = (int)cond[best_j].size() - 2; i >= p_best; --i) {
                    int next_v = cond[best_j][i];
                    if (next_v > target_v && next_v < curr_top) {
                        target_v = next_v;
                    } else {
                        break;
                    }
                }
                
                move_box(target_v, curr);
                carry_out();
            } else {
                break;
            }
        }
        
        // k回目の処理が終わり、curr列に積まれたソート済みの箱を保護対象にする
        protected_size[curr] = (int)cond[curr].size();
    }
}

void solve_initial() {
    cond = initial_cond;
    cnt_val = 1;
    ans.clear();
    cost = 0;
    capa.assign(m, n / m);
    bottom_ok.assign(m, 0);
    bottom_cnt = n;

    apply_preprocess();

    while (cnt_val <= n) {
        carry_out();
        bottom_carry_out();
        for (int j = 0; j < m; ++j) {
            if (capa[j] == bottom_ok[j]) {
                move_box(bottom_cnt, j);
                break;
            }
            if (find(cond[j].begin(), cond[j].end(), cnt_val) != cond[j].end()) {
                int idousaki = min_max();
                int hantei = *min_element(cond[idousaki].begin(), cond[idousaki].end());
                for (int i = (int)cond[j].size() - 1; i >= 1; --i) {
                    if (cond[j][i] == cnt_val) {
                        if (cond[j][i] == cond[j].back()) break;
                        move_box(cond[j][i + 1], idousaki);
                        break;
                    }
                    if (cond[j][i] < hantei) {
                        if (cond[j][i] == cond[j].back()) continue;
                        move_box(cond[j][i + 1], idousaki);
                        idousaki = min_max();
                        hantei = *min_element(cond[idousaki].begin(), cond[idousaki].end());
                    }
                }
            }
        }
    }
    if (cost < best_score) {
        best_score = cost;
        best_ans = ans;
    }
}

void solve_grid(int const_val, int key, int key2) {
    cond = initial_cond;
    cnt_val = 1;
    ans.clear();
    cost = 0;
    capa.assign(m, n / m);
    bottom_ok.assign(m, 0);
    bottom_cnt = n;

    apply_preprocess();

    while (cnt_val <= n) {
        carry_out();
        bottom_carry_out();
        for (int j = 0; j < m; ++j) {
            if (capa[j] == bottom_ok[j] && cnt_val < const_val) {
                int idousaki = min_max();
                int fro = -1;
                for (int i = 0; i < m; ++i) {
                    if (find(cond[i].begin(), cond[i].end(), bottom_cnt) != cond[i].end()) {
                        fro = i;
                        break;
                    }
                }
                if (fro != -1) {
                    for (int i = (int)cond[fro].size() - 1; i >= 1; --i) {
                        if (cond[fro][i] == bottom_cnt) break;
                        if (cond[fro][i] == cond[fro].back()) continue;
                        if (cond[fro][i] < cnt_val + key) {
                            move_box(cond[fro][i + 1], idousaki);
                            idousaki = min_max();
                        }
                    }
                }
                move_box(bottom_cnt, j);
                break;
            }
            if (find(cond[j].begin(), cond[j].end(), cnt_val) != cond[j].end()) {
                int idousaki = min_max();
                int hantei = *min_element(cond[idousaki].begin(), cond[idousaki].end());
                for (int i = (int)cond[j].size() - 1; i >= 1; --i) {
                    if (cond[j][i] == cnt_val) {
                        if (cond[j][i] == cond[j].back()) break;
                        if (cnt_val >= const_val) {
                            for (int k = 0; k < m; ++k) {
                                if (capa[k] == bottom_ok[k]) {
                                    idousaki = k;
                                    break;
                                }
                            }
                        }
                        move_box(cond[j][i + 1], idousaki);
                        break;
                    }
                    if (cond[j][i] < hantei - key2 + 15) {
                        if (cond[j][i] == cond[j].back()) continue;
                        move_box(cond[j][i + 1], idousaki);
                        idousaki = min_max();
                        hantei = *min_element(cond[idousaki].begin(), cond[idousaki].end());
                    }
                }
            }
        }
    }
    if (cost < best_score) {
        best_score = cost;
        best_ans = ans;
    }
}

int main() {
    auto start_time = chrono::system_clock::now(); // タイマー開始

    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    if (!(cin >> n >> m)) return 0;

    initial_cond.resize(m);
    for (int i = 0; i < m; ++i) {
        initial_cond[i].push_back(1000000000); // 番兵
        for (int j = 0; j < n / m; ++j) {
            int val;
            cin >> val;
            initial_cond[i].push_back(val);
        }
    }

    current_perm.resize(m);
    iota(current_perm.begin(), current_perm.end(), 0);

    vector<int> const_vals = {140, 150, 160};
    uniform_int_distribution<int> dist_const(0, 2);
    uniform_int_distribution<int> dist_key(0, 39);
    uniform_int_distribution<int> dist_key2(5, 29);

    int loop_cnt = 0;
    // 1.8秒経過するまで、ランダムな順列とパラメータの組み合わせを試し続ける
    while (true) {
        // 毎回時間チェックすると遅いので、64回に1回だけ確認して高速化
        if ((loop_cnt & 63) == 0) {
            auto now = chrono::system_clock::now();
            double elapsed = chrono::duration_cast<chrono::duration<double>>(now - start_time).count();
            if (elapsed > 1.8) break;
        }
        loop_cnt++;

        // 毎回順列をシャッフルする（これが多様性を生んで強かった理由です）
        shuffle(current_perm.begin(), current_perm.end(), mt);

        // 10回に1回は solve_initial の固定ロジックを試す
        if (loop_cnt % 10 == 0) {
            solve_initial();
        } else {
            // 残りはランダムなパラメータで solve_grid を試す
            int c_val = const_vals[dist_const(mt)];
            int k = dist_key(mt);
            int k2 = dist_key2(mt);
            solve_grid(c_val, k, k2);
        }
    }

    // 最適な操作列を出力
    for (auto p : best_ans) {
        cout << p.first << " " << p.second << "\n";
    }

    return 0;
}