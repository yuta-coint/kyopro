#include <bits/stdc++.h>
using namespace std;

using ll = long long;

// ========================================
// 乱数
// ========================================
mt19937 rng(
    chrono::steady_clock::now().time_since_epoch().count()
);

double rand01() {
    static uniform_real_distribution<double> dist(0.0, 1.0);
    return dist(rng);
}

int randint(int l, int r) {
    // [l, r]
    return uniform_int_distribution<int>(l, r)(rng);
}


// ========================================
// 問題依存部分
// ========================================

struct State {
    vector<int> p;
    double score;
};

struct Move {
    int i, j;

    // 必要ならここに操作の種類などを追加
    // int type;
};


// 初期解を作る
State make_initial_state(int N) {
    State state;

    state.p.resize(N);
    iota(state.p.begin(), state.p.end(), 0);

    // 必要に応じて変更
    shuffle(state.p.begin(), state.p.end(), rng);

    state.score = 0.0;  // 後で calc_score で更新

    return state;
}


// スコアを全計算
double calc_score(const State& state) {
    double score = 0.0;

    // TODO:
    // 問題に応じて実装

    return score;
}


// 近傍をランダムに生成
Move generate_move(const State& state) {
    int N = state.p.size();

    int i = randint(0, N - 1);
    int j = randint(0, N - 1);

    while (i == j) {
        j = randint(0, N - 1);
    }

    return {i, j};
}


// moveを適用したときの
//
// new_score - current_score
//
// を返す
double calc_diff(const State& state, const Move& move) {
    int i = move.i;
    int j = move.j;

    double diff = 0.0;

    // TODO:
    // 問題に応じて差分計算

    return diff;
}


// 実際に状態を変更する
void apply_move(State& state, const Move& move) {
    int i = move.i;
    int j = move.j;

    swap(state.p[i], state.p[j]);

    // calc_diffを使っているなら、
    // score自体は焼きなまし側で更新する
}


// ========================================
// 焼きなまし本体
// ========================================

State simulated_annealing(
    State initial_state,
    double time_limit,
    double start_temp,
    double end_temp
) {
    State current = initial_state;
    current.score = calc_score(current);

    State best = current;

    auto start_time = chrono::steady_clock::now();

    long long iteration = 0;

    double temp = start_temp;

    while (true) {
        iteration++;

        // -------------------------
        // 時間・温度更新
        // -------------------------
        if ((iteration & 255) == 0) {
            double elapsed =
                chrono::duration<double>(
                    chrono::steady_clock::now() - start_time
                ).count();

            if (elapsed >= time_limit) {
                break;
            }

            double progress = elapsed / time_limit;

            // 指数冷却
            temp =
                start_temp
                * pow(end_temp / start_temp, progress);
        }

        // -------------------------
        // 近傍生成
        // -------------------------
        Move move = generate_move(current);

        // -------------------------
        // 差分計算
        // -------------------------
        double diff = calc_diff(current, move);

        // -------------------------
        // 採用判定
        //
        // 最大化
        // -------------------------
        if (
            diff >= 0.0
            || rand01() < exp(diff / temp)
        ) {
            apply_move(current, move);

            current.score += diff;

            if (current.score > best.score) {
                best = current;
            }
        }
    }

    cerr << "iteration = " << iteration << '\n';
    cerr << "best score = " << best.score << '\n';

    return best;
}


// ========================================
// main
// ========================================

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    // 必要な入力を読む

    State initial = make_initial_state(N);

    const double TIME_LIMIT = 1.9;

    // 問題に応じて調整
    const double START_TEMP = 100.0;
    const double END_TEMP = 0.01;

    State answer = simulated_annealing(
        initial,
        TIME_LIMIT,
        START_TEMP,
        END_TEMP
    );

    for (int x : answer.p) {
        cout << x << ' ';
    }
    cout << '\n';

    return 0;
}