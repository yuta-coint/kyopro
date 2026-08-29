#include <bits/stdc++.h>
using namespace std;
#define ll long long

array<ll, 3> generalized_floor_sum(ll n, ll m, ll a, ll b) {
    ll a1 = a / m, a2 = a % m;
    ll b1 = b / m, b2 = b % m;
    ll k = (a2 * (n - 1) + b2) / m;

    ll s_01 = n * (n - 1) / 2 * a1 + b1 * n;
    ll s_11 = n * (n - 1) / 2 * b1 + n * (2 * n - 1) * (n - 1) / 6 * a1;
    ll s_02 = n * (n - 1) * (2 * n - 1) / 6 * a1 * a1 + n * (n - 1) * a1 * b1 + n * b1 * b1 + 2 * a1 * n * (n - 1) / 2 * k + 2 * b1 * n * k;

    if (a2 == 0) {
        return {s_01, s_11, s_02};
    }

    auto [gfs_01, gfs_11, gfs_02] = generalized_floor_sum(k, a2, m, m + a2 - b2 - 1);

    ll res_01 = s_01 + n * k - gfs_01;
    ll res_11 = s_11 + n * (n - 1) / 2 * k + (gfs_01 - gfs_02) / 2;
    ll res_02 = s_02 + n * k * k + (-2 * b1 - 1 + a1) * gfs_01 - 2 * gfs_11 - a1 * gfs_02;

    return {res_01, res_11, res_02};
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int T;
    if (!(cin >> T)) return 0;

    while (T--) {
        ll N, M, A, B1, B2;
        cin >> N >> M >> A >> B1 >> B2;
        
        if (B1 > B2) {
            swap(B1, B2);
        }

        ll ans = A * A * N * (N - 1) * (2 * N - 1) / 6 + (B1 + B2) * A * N * (N - 1) / 2 + B1 * B2 * N;
        ans *= 2;

        auto [gfsb1_01, gfsb1_11, gfsb1_02] = generalized_floor_sum(N, M, A, B1);
        auto [gfsb2_01, gfsb2_11, gfsb2_02] = generalized_floor_sum(N, M, A, B2);

        ans -= 2 * A * M * gfsb1_11;
        ans -= 2 * A * M * gfsb2_11;
        ans += (M * M - 2 * B2 * M) * gfsb1_01;
        ans += (-2 * B1 * M - M * M) * gfsb2_01;
        ans += M * M * gfsb1_02;
        ans += M * M * gfsb2_02;

        cout << ans / 2 << "\n";
    }

    return 0;
}