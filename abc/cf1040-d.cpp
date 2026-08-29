#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
// https://zenn.dev/reputeless/books/standard-cpp-for-competitive-programming/viewer/binary-indexed-tree
class BIT
{
public:

	BIT() = default;

	// 長さ size の数列で初期化
	explicit BIT(size_t size)
		: m_bit(size + 1) {}

	// 数列で初期化
	explicit BIT(const vector<long long>& v)
		: BIT(v.size())
	{
		for (int i = 0; i < static_cast<int>(v.size()); ++i)
		{
			add((i + 1), v[i]);
		}
	}

	// 閉区間 [1, r] の合計を返す (1-based indexing)
	long long sum(int r) const
	{
		long long ret = 0;

		for (; 0 < r; r -= (r & -r))
		{
			ret += m_bit[r];
		}

		return ret;
	}

	// 閉区間 [l, r] の合計を返す (1-based indexing)
	long long sum(int l, int r) const
	{
		return (sum(r) - sum(l - 1));
	}

	// 数列の i 番目の要素を加算 (1-based indexing)
	void add(int i, long long value)
	{
		for (; i < static_cast<int>(m_bit.size()); i += (i & -i))
		{
			m_bit[i] += value;
		}
	}

private:

	vector<long long> m_bit;
};

int solve(){
    int N;
    cin >> N;
    vector<int> A(N);
    vector<ll> T(N);
    for (int i = 0; i < N; i++){
        int t;
        cin >> t;
        A[t-1] = i;
        T[i] = 1;
    }
    ll ans = 0;
    BIT S(T);
    ll cnt = N;
    for (int i = 0; i < N; i++){
        S.add(A[i], -1);
        cnt -= 1;
        ll k = S.sum(A[i], N);
        ans += min(k, cnt - k);
    }
    cout << ans << endl;
    return 0;
}
int main(){
    int T;
    cin >> T;
    for (int i = 0; i < T; i++){
        solve();
    }
    return 0;
}