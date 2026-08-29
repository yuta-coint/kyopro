#include <bits/stdc++.h>
using namespace std;
int main() {
    int N,L,R;
    int ans;
    ans = 0;
    cin >> N >> L >> R;
    for (int i = 0; i < N; i++) {
        int X,Y;
        cin >> X >> Y;
        if (X <= L && Y >= R) {
            ans += 1;
        }
    }
    cout << ans << endl;
}