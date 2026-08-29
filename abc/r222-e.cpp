#include <bits/stdc++.h>
using namespace std;

chrono::steady_clock::time_point start;

#define FOR(i, a, b) for (int i = a; i < int(b); ++i)
#define FOR_R(i, a, b) for (int i = int(b) - 1; i >= a; --i)
template <typename T>
using vc = vector<T>;

int popcnt(int x) { return __builtin_popcount(x); }

template <int mod>
struct modint {
  using u32 = uint32_t;
  using u64 = uint64_t;
  static constexpr u32 umod = u32(mod);
  static_assert(umod < u32(1) << 31);
  u32 val;
  constexpr modint() : val(0) {}
  constexpr modint(int x) : val((x %= mod) < 0 ? x + mod : x){};
  modint &operator+=(const modint &p) {
    if ((val += p.val) >= umod) val -= umod;
    return *this;
  }
  modint &operator-=(const modint &p) {
    if ((val += umod - p.val) >= umod) val -= umod;
    return *this;
  }
  modint &operator*=(const modint &p) {
    val = u64(val) * p.val % umod;
    return *this;
  }
  modint operator-() const { return modint(-val); }
  modint operator+(const modint &p) const { return modint(*this) += p; }
  modint operator-(const modint &p) const { return modint(*this) -= p; }
  modint operator*(const modint &p) const { return modint(*this) *= p; }
};

using mint = modint<998244353>;

template <typename T>
void hadamard(vc<T> &a) {
  int n = a.size();
  assert(n > 0 && (n & (n - 1)) == 0);
  for (int len = 1; len < n; len <<= 1) {
    for (int i = 0; i < n; i += len << 1) {
      FOR(j, 0, len) {
        T x = a[i + j];
        T y = a[i + j + len];
        a[i + j] = x + y;
        a[i + j + len] = x - y;
      }
    }
  }
}

template <typename T>
vc<T> xor_convolution(vc<T> a, vc<T> b) {
  assert(a.size() == b.size());
  int n = a.size();
  assert(n > 0 && (n & (n - 1)) == 0);

  hadamard(a);
  hadamard(b);
  FOR(i, 0, n) a[i] *= b[i];
  hadamard(a);
  FOR(i, 0, n) a[i] /= n;
  return a;
}

template <typename T>
vc<T> xor_square(vc<T> a) {
  int n = a.size();
  assert(n > 0 && (n & (n - 1)) == 0);

  hadamard(a);
  FOR(i, 0, n) a[i] *= a[i];
  hadamard(a);
  FOR(i, 0, n) a[i] /= n;
  return a;
}

vc<int> solve(int n, const vc<int> &a, const vc<int> &b) {
  int N = 1 << n;
  vc<mint> A(N), B(N);
  FOR(S, 0, N) A[S] = a[S];
  FOR(S, 0, N) B[S] = b[S];

  // x = y - 1
  for (int i = 1; i != N; i <<= 1) {
    for (int j = 0; j != N; j += i << 1) {
      for (int k = 0; k != i; k++) {
        A[j + k] -= A[i + j + k];
        B[j + k] -= B[i + j + k];
      }
    }
  }

  vc<array<mint, 21>> RA(N), RB(N);
  FOR(S, 0, N) RA[S][popcnt(S)] = A[S], RB[S][popcnt(S)] = B[S];

  // ranked zeta
  for (int i = 1; i != N; i <<= 1) {
    for (int j = 0; j != N; j += i << 1) {
      for (int k = 0; k != i; k++) {
        FOR(d, 0, n + 1) RA[i + j + k][d] += RA[j + k][d];
        FOR(d, 0, n + 1) RB[i + j + k][d] += RB[j + k][d];
      }
    }
  }

  // pointwise product
  FOR(S, 0, N) {
    array<mint, 41> prod{};
    FOR(i, 0, n + 1) FOR(j, 0, n + 1) prod[i + j] += RA[S][i] * RB[S][j];
    // x^2 -> 2x
    FOR_R(i, 0, 2 * n) prod[i] += prod[i + 1] + prod[i + 1];
    FOR(i, 0, n + 1) RA[S][i] = prod[i];
  }

  // ranked mobius
  for (int i = 1; i != N; i <<= 1) {
    for (int j = 0; j != N; j += i << 1) {
      for (int k = 0; k != i; k++) {
        FOR(d, 0, n + 1) RA[i + j + k][d] -= RA[j + k][d];
      }
    }
  }

  FOR(S, 0, N) A[S] = RA[S][popcnt(S)];

  // y = x + 1
  for (int i = 1; i != N; i <<= 1) {
    for (int j = 0; j != N; j += i << 1) {
      for (int k = 0; k != i; k++) {
        A[j + k] += A[i + j + k];
      }
    }
  }

  vc<int> ans(N);
  FOR(S, 0, N) ans[S] = A[S].val;
  return ans;
}

int main() {
  ios_base::sync_with_stdio(false);
  std::cin.tie(nullptr);
  auto start = chrono::steady_clock::now();
  int n,m;
  cin >> n >> m;
  vc<int> A(1<<m);
  int temp;
  FOR(S, 0, n){
    cin >> temp;
    A[temp] += 1;
  }
  vc<mint> ten_pow(1 << m);
  mint pw = 1;
  FOR(S, 0, 1 << m){
    ten_pow[S] = pw;
    pw *= 10;
  }

  mint ans;
  int cnt = 0;
  while (true){
    auto now = chrono::steady_clock::now();
        double elapsed =
            chrono::duration<double>(now - start).count();
    if (elapsed > 2.0) break;
    cnt += 1;
    vc<long long> C(1 << m);
    FOR(S, 0, 1 << m){
      if (A[S] >= cnt){
        C[S] = 1;
      }
    }
    vc<long long> prod = xor_square(C);
    FOR(S, 1, 1 << m) {
      ans += mint(int(prod[S]))*ten_pow[S];
    }
  }
  vc<int> amari;
  int len_amari = 0;
  FOR(S, 0, 1 << m) {
    ans += mint(2)*mint(A[S]/2);
    if (A[S] > cnt){
      amari.push_back(S);
      len_amari += 1;
    }
  }
  FOR(S, 0, len_amari){
    FOR(Q, 0, len_amari){
      if (amari[S]!=amari[Q]){
        int k = min(A[amari[S]],A[amari[Q]]);
        ans += mint(k - cnt)*ten_pow[amari[S]^amari[Q]];
      }
    }
  }
  ans *= 499122177;
  cout << ans.val << endl;
  return 0;
}
